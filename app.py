from flask import Flask
app = Flask(__name__)


@app.route("/amber")
def amber():
    return "Moon Prism Power!"

if __name__ == "__main__":
    app.run()

