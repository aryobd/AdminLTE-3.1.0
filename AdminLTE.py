# https://en.wikipedia.org/wiki/Flask_(web_framework)

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main() -> str:
    return render_template("index.html")

@app.route("/index2")
def index2() -> str:
    return render_template("index2.html")

@app.route("/index3")
def index3() -> str:
    return render_template("index3.html")

if __name__ == "__main__":
    app.run(debug = True)
