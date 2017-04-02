from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/Kizzie")
def Kizzie():
	return "Hello, Kizzie!"
	
if __name__ == "__main__":
    app.run()

