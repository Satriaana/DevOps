import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import dotenv_values

config = dotenv_values(".env")

sender_email = str(config['ISSUELIST_MAIL'])
password = str(config['ISSUELIST_PASSWORD'])
SMTP_SERVER = str(config['SMTP_SERVER'])
SMTP_PORT = int(str(config['SMTP_PORT']))


def SendMail(client, html, pm):
    message = MIMEMultipart("alternative")
    message["Subject"] = f"Issue list for {pm}"
    message["From"] = sender_email
    message["To"] = client
    part2 = MIMEText(html, "html")

    message.attach(part2)
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=context) as server:
        try:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, client, message.as_string()
            )
        except Exception as e:
            print(e)
