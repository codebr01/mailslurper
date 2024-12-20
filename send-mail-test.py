import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SMTP_SERVER="localhost"
SMPT_PORT=2500

FROM_EMAIL="origem@gmail.com"
TO_EMAIL="destino@gmail.com"
SUBJECT="Teste de Email com MailSlurper"
BOBY="Olá, este é um email de teste enviado via MailSlurper no Docker."

msg = MIMEMultipart()
msg['From'] = FROM_EMAIL
msg['To'] = TO_EMAIL
msg['Subject'] = SUBJECT

msg.attach(MIMEText(BOBY, 'plain', 'utf-8'))
try:
    with smtplib.SMTP(SMTP_SERVER, SMPT_PORT,) as server:
        server.sendmail(FROM_EMAIL, TO_EMAIL, msg.as_string())
        print('Email enviado com sucesso')
except Exception as e:
    print(f'Erro ao enviar o email: {e}')