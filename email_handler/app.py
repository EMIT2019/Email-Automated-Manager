from flask import Flask
from sender import EmailSender
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

@app.route("/")
def test() -> str:
    return "<p>Hello World. Greetings from EMIT's computer.<p>"

@app.route("/send")
def send_mail() -> str:
    host:str = os.getenv("EMAIL_HOST")
    sender:str = os.getenv("EMAIL_SENDER")
    password:str = os.getenv("EMAIL_PASSWORD")
    port:int = int(os.getenv("EMAIL_PORT"))
    addresse:list[str] = ["emilianoandreurbinazavala@gmail.com"]
    email_content:dict = {
        "subject":"This is a test from EMIT's PC.",
        "body":"THIS IS JUST A TEST DO NOT MIND ABOUT IT"
    }

    new_sender:EmailSender = EmailSender(host, sender, password, port)
    mail_status:bool = new_sender.send_email(addresse, email_content)
    print(f"Mail Status: {mail_status}")    
    return "<p>The mail was succesfully sent!!!<p>"

if __name__ == "__main__":
    app.run()