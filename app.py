from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/Xin")
def Xin():
	return "Hello, Xin!"

if __name__ == "__main__":
    app.run()
