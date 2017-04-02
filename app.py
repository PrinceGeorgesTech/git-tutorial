from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/David")
def myname():
    return "Hello, David!"
if __name__ == "__main__":
    app.run()
