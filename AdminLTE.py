# https://en.wikipedia.org/wiki/Flask_(web_framework)

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main() -> str:
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=False)
