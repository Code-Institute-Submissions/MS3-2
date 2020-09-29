import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

from os import path
if path.exists("env.py"):
  import env


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'user_uploads'
app.config["MONGO_URI"] = os.getenv('MONGO_URI')



#os.getenv('MONGO_URI', 'mongodb://localhost')


mongo = PyMongo(app)



@app.route("/")
def index():
  return render_template("index.html")


@app.route("/flaskmongo")
def flaskmongo():
    return render_template("flaskmongo.html", books=mongo.db.books.find())



@app.route("/submit", methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        book_name = request.form["book_name"]
        author_name = request.form["author_name"]
       # genre = request.form["genre"]
        summary = request.form["summary"]
        added_by = request.form["added_by"]
        print (book_name, author_name, summary, added_by)
    return render_template("submit.html", page_title="Submit")
   



 #@app.route('/accept_data', methods=['post'])
#def accept_data():
 # path = request.form["{{ url_for('submit.html') }}"]

@app.route("/browse")
def browse():
    return render_template("browse.html", page_title="Browse")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)