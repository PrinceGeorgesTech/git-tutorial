from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/myname")
def myname():
    return "Hello, My Name!"
    
if __name__ == "__main__":
    app.run()
