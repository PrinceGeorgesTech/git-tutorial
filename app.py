from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"
@app.route("/Kwame")
def Qat():
    return "Hello, World KwameB!"

@app.route("/chuck")
def chuck():
    return "Hello, Chuck!"

@app.route("/ruby")
def ruby():
    return "Hello, RUBY!"


if __name__ == "__main__":
    app.run()
