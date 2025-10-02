import socket
import threading
import json
from typing import Dict, Any

# transformers는 처음 실행 시 모델을 다운로드합니다.
# 사내/오프라인 환경이면 사전 캐시 필요.
from transformers import pipeline

HOST = "127.0.0.1"
PORT = 9000
BACKLOG = 5
BUFF = 4096
ENC = "utf-8"

# ---- AI 파이프라인 초기화 (필요 시 모델 변경 가능) ----
sentiment = pipeline("sentiment-analysis")  # distilbert-base-uncased-finetuned-sst-2-english
summarizer = pipeline("summarization")      # t5-small/sshleifer-distilbart-cnn-12-6 등 환경에 따라

def handle_request(payload: Dict[str, Any]) -> Dict[str, Any]:
    task = payload.get("task")
    text = payload.get("text", "")

    if not text or not isinstance(text, str):
        return {"ok": False, "error": "text must be a non-empty string"}

    if task == "sentiment":
        result = sentiment(text)[0]   # {'label': 'POSITIVE', 'score': 0.999...}
        return {"ok": True, "task": "sentiment", "label": result["label"], "score": result["score"]}

    elif task == "summary":
        # 매우 긴 텍스트는 간단히 길이 제한. 필요시 슬라이딩 윈도우로 분할 요약 가능.
        max_len = 1500
        input_text = text[:max_len]
        out = summarizer(input_text, max_length=120, min_length=25, do_sample=False)[0]["summary_text"]
        return {"ok": True, "task": "summary", "summary": out}

    else:
        return {"ok": False, "error": f"unknown task: {task}. Use 'sentiment' or 'summary'."}

def client_thread(conn: socket.socket, addr):
    with conn:
        try:
            # 간단한 프로토콜: "한 줄에 하나의 JSON" (newline-delimited JSON)
            buffer = ""
            conn.sendall(b'{"hello":"ai-server","protocol":"ndjson","tasks":["sentiment","summary"]}\n')
            while True:
                data = conn.recv(BUFF)
                if not data:
                    break
                buffer += data.decode(ENC)

                # 줄 단위로 파싱
                while "\n" in buffer:
                    line, buffer = buffer.split("\n", 1)
                    if not line.strip():
                        continue
                    try:
                        payload = json.loads(line)
                        resp = handle_request(payload)
                    except json.JSONDecodeError:
                        resp = {"ok": False, "error": "invalid JSON"}

                    msg = (json.dumps(resp, ensure_ascii=False) + "\n").encode(ENC)
                    conn.sendall(msg)
        except ConnectionResetError:
            pass
        finally:
            print(f"Disconnected: {addr}")

def main():
    print(f"Loading AI pipelines... (first run may download models)")
    # 파이프라인이 위에서 이미 준비되며, 여기서 로딩 메시지를 알림
    print("Starting socket server...")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(BACKLOG)
        print(f"AI Server listening on {HOST}:{PORT}")

        while True:
            conn, addr = s.accept()
            print(f"Connected: {addr}")
            threading.Thread(target=client_thread, args=(conn, addr), daemon=True).start()

if __name__ == "__main__":
    main()
