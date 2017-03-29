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
    return "Hello, Mr.Gabriel!"
  
@app.route("/ANAJAVED")
def ANAJAVED():
    return "Hello, ANA!"


if __name__ == "__main__":
    app.run()
