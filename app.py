import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
  import env


app = Flask(__name__)
app.secret_key = env.Secret_Key
app.config["MONGO_DBNAME"] = 'user_uploads'
app.config["MONGO_URI"] = os.getenv('MONGO_URI')
mongo = PyMongo(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/submit")
def submit():
    return render_template("submit.html", page_title="Submit")


@app.route('/insert_book', methods=['POST'])
def insert_book():
    books = mongo.db.books
    books.insert_one(request.form.to_dict())
    return redirect(url_for('browse'))


@app.route("/browse")
def browse():
    return render_template("browse.html", page_title="Browse",
    books=mongo.db.books.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)