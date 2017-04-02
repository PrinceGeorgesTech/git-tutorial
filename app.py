from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/Peg")
def myname():
    return "Hello, My Name is Peg!"

if __name__ == "__main__":
    app.run()
