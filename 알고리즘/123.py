import re

# 정규 표현식으로 토큰 패턴 정의
token_specification = [
    ("NUMBER",   r'\d+(\.\d+)?'),   # 정수 또는 실수
    ("PLUS",     r'\+'),            # +
    ("MINUS",    r'-'),             # -
    ("TIMES",    r'\*'),            # *
    ("DIVIDE",   r'/'),             # /
    ("LPAREN",   r'\('),            # (
    ("RPAREN",   r'\)'),            # )
    ("SKIP",     r'[ \t]+'),        # 공백 무시
    ("MISMATCH", r'.'),             # 알 수 없는 문자
]

# 정규식을 하나로 합치기
tok_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specification)

def lexer(code):
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        if kind == "NUMBER":
            value = float(value) if '.' in value else int(value)
            yield (kind, value)
        elif kind == "SKIP":
            continue
        elif kind == "MISMATCH":
            raise RuntimeError(f"Unexpected character: {value}")
        else:
            yield (kind, value)

# 테스트
expr = "12.5 + (3 - 2) * 10 / 5"
print("Input:", expr)
print("Tokens:")
for token in lexer(expr):
    print(token)