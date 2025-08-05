from flask import Flask

app = Flask(__name__)

@app.route("/")
def test() -> str:
    return "<p>Hello World. Greetings from EMIT's computer.<p>"

if __name__ == "__main__":
    app.run()