import os
from flask import Flask, render_template
from flask_pymongo import flask_pymongo
from bson.objectid import objectid

app = Flask(__name__)


@app.route("/")
def index():
  return render_template("index.html")


@app.route("/create")
def create():
    return render_template("create.html", page_title="Create")

@app.route("/browse")
def browse():
    return render_template("browse.html", page_title="Browse")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)