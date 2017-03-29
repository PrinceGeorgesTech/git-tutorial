from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/gabriel")
def gabriel():
    return "Hello, Ms. Wright!"

@app.route("/fareed")
def fareed():
    return "Hello, Mr.Fareed!"

@app.route("/ANAJAVED")
def ANAJAVED():
    return "Hello, ANA!"

@app.route("/nick")
def hello():
    return "Hello, Mr.Nick!"

if __name__ == "__main__":
    app.run()
