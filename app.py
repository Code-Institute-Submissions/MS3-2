import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')
app.config["MONGO_DBNAME"] = 'user_uploads'
app.config["MONGO_URI"] = os.getenv('MONGO_URI')
mongo = PyMongo(app)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html", page_title="About")


@app.route('/submit')
def submit():
    return render_template("submit.html", page_title="Submit")


""" Retrieves all the 'books' from our MongoDB and
displays them on browse.html"""


@app.route('/browse')
def browse():
    return render_template("browse.html", page_title="Browse",
                           books=mongo.db.books.find())


""" insert_book function runs when the submit button is clicked.
It converts info to a dictionary and adds it to the DB.
It then redirects the user to the browse.html page where they
can view their upload and the rest of the uploads to the site.
 """


@app.route('/insert_book', methods=['POST'])
def insert_book():
    books = mongo.db.books
    books.insert_one(request.form.to_dict())
    return redirect(url_for('browse'))

@app.route('/edit_book<book_id>')
def edit_book(book_id):
    the_book =  mongo.db.tasks.find_one({"_id": ObjectId(book_id)})
    return render_template('editbook.html', book=the_book)


""" The delete_book function allows the user completely
delete their upload ftom the database """


@app.route('/delete_book/<book_id>')
def delete_book(book_id):
    mongo.db.books.remove({'_id': ObjectId(book_id)})
    return redirect(url_for('browse'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
