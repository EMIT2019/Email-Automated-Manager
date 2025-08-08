import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
class EmailSender():
    def __init__(self, host:str, sender:str, password:str, port:int, email_content:dict = None):
        self.host = host
        self.sender = sender
        self.password = password
        self.port = port
        self.email_content = email_content

    def send_email(self, addresse:list[str], email_content:dict = None) -> bool:
        try:
            message:MIMEMultipart = MIMEMultipart()
            subject:str = email_content["subject"] if email_content is not None else self.email_content["subject"]
            message["Subject"] = subject
            message["From"] = self.sender
            message["To"] = ", ".join(addresse)
            body:str = email_content["body"] if email_content is not None else self.email_content["body"]
            message.attach(MIMEText(body, 'plain'))
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(self.host, self.port, context=context) as server:
                server.login(self.sender, self.password)
                server.sendmail(self.sender, addresse, message.as_string())
            return True
        except Exception as ex:
            print(f"There was an error: {ex}")
            return False