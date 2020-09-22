import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
  return render_template("index.html")


@app.route("/create")
def create():
    return render_template("create.html")

@app.route("/browse")
def browse():
    return render_template("browse.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)