import os
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def index():
  return render_template("index.html")


@app.route("/submit", methods=['get','post'])
def submit():
  #  book_name = request.form["book_name"]
  #  author_name = request.form["author_name"]
  #  genre = request.form["genre"]
  #  added_by = request.form["added_by"]
  #  review= request.form["review"]
  #  print (book_name, review)
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