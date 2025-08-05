import smtplib, ssl

class EmailSender():
    def __init__(self):
        pass

    def send_email(self) -> bool:
        try:
            port:int = 465
            smtp_server:str = "smtp.gmail.com"
            sender:str = "emilianoandreurbinazavala@gmail.com"
            addresse:str = "emilianoandreurbinazavala@gmail.com"
            password:str = ""
            message:str = "Subject: This is only a test   \n this message was send from python"
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender, password)
                server.sendmail(sender, addresse, message)
        except Exception as ex:
            print(f"There was an error: {ex}")

test = EmailSender()
test.send_email()