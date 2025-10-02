import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587  # STARTTLS
USER = "qkrwhdgur0319@gmail.com"          # 전체 이메일 주소
APP_PASSWORD = "ovzp rauv qgod wkok"   # 16자리 앱 비밀번호(공백 없이 붙여써도 됩니다)

TO = "qkrwhdgur0319@kookmin.ac.kr"

msg = MIMEMultipart()
msg["From"] = USER
msg["To"] = TO
msg["Subject"] = "SMTP 테스트(STARTTLS)"
msg.attach(MIMEText("테스트 본문입니다.", "plain"))

server = smtplib.SMTP(SMTP_HOST, SMTP_PORT)
server.set_debuglevel(1)          # 문제 시 상세 로그 확인용
server.ehlo()
server.starttls()
server.ehlo()
server.login(USER, APP_PASSWORD)  # 앱 비밀번호 사용
server.sendmail(USER, TO, msg.as_string())
server.quit()
