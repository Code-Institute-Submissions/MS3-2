""" app.py contains all routes and functions used in the site """

import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)
""" Create an instance of Flask """
app.secret_key = os.getenv('SECRET_KEY')
app.config["MONGO_DBNAME"] = 'user_uploads'
app.config["MONGO_URI"] = os.getenv('MONGO_URI')
mongo = PyMongo(app)


@app.route('/')
def index():
    """ index() renders our "index.html" homepage """
    return render_template("index.html", block_title="Home")


@app.route('/about')
def about():
    """ about() renders our "about.html" page """
    return render_template("about.html", page_title="About")


@app.route('/submit')
def submit():
    """ submit() renders our "submit.html" page.
    Accesses genres collection in MongoDB """
    return render_template("submit.html", page_title="Submit",
                           genres=mongo.db.genres.find())


@app.route('/browse')
def browse():
    """ browse() retrieves all 'books' and 'genres' from MongoDB
    and displays them on browse.html """
    return render_template("browse.html", page_title="Browse",
                           books=mongo.db.books.find(),
                           genres=mongo.db.genres.find())


@app.route('/insert_book', methods=['POST'])
def insert_book():
    """ insert_book function runs when the submit button is clicked.
    It converts info to a dictionary and adds it to the DB.
    It then redirects the user to the browse.html page where they
    can view their upload and the rest of the uploads to the site.
    """
    books = mongo.db.books
    books.insert_one(request.form.to_dict())
    return redirect(url_for('browse'))


@app.route('/edit_book/<book_id>')
def edit_book(book_id):
    """ On pressing the 'Edit' button on browse.html,
    the edit_book function brings the user to 'editbook.html
    where they can edit previously added data
    """
    the_book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    all_genres = mongo.db.genres.find()
    return render_template('editbook.html', book=the_book, genres=all_genres)


@app.route('/delete_book/<book_id>')
def delete_book(book_id):
    """ The delete_book function allows the user completely
    delete their upload from the database """
    mongo.db.books.remove({'_id': ObjectId(book_id)})
    return redirect(url_for('browse'))


if __name__ == '__main__':
    """ Setting up our IP Address and Port number """
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=False)
