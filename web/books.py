from flask import(
  Blueprint, render_template, request, redirect, url_for)

from web.bookdb import get_db
from web.files import save_img, write_file

bp = Blueprint('books', __name__)

@bp.route('/books', methods=['GET'])
def all():
  db = get_db()
  alldata = db.execute('SELECT * FROM books').fetchall()
  return render_template('books/all.html', books=alldata)

@bp.route('/books/new', methods=['GET','POST'])
def new():
  db = get_db()
  if request.method == 'POST':
    title = request.form['title']
    author = request.form['author']
    db = get_db()
    db.execute("INSERT INTO books(title,author) VALUES(?,?)",(title,author))
    db.commit()
    return redirect(url_for('books.all'))

  authors = db.execute('SELECT * FROM authors').fetchall()
  return render_template('books/new.html',authors=authors)

@bp.route('/books/show/<book_id>', methods=['GET'])
def show(book_id):
  db = get_db()
  book = db.execute('SELECT * FROM books where id=?', book_id).fetchone()
  return render_template('books/show.html',book=book)

@bp.route('/books/delete/<book_id>', methods=['GET'])
def delete(book_id):
  db = get_db()
  db.execute('DELETE FROM books where id=?', book_id)
  db.commit()
  return redirect(url_for('books.all'))

@bp.route('/books/edit/<book_id>', methods=['GET','POST'])
def edit(book_id):
  db = get_db()
  if request.method == 'POST':
    name = request.form['name']
    bio = request.form['bio']
    db.execute("UPDATE books SET name=?, bio=? where id=?",(name,bio,book_id))
    db.commit()
    return redirect(url_for('books.all'))

  book = db.execute('SELECT * FROM books where id=?',book_id).fetchone()
  return render_template('books/edit.html',book=book)

@bp.route('/books/upload/<book_id>', methods=['GET','POST'])
def upload(book_id):
  db = get_db()
  if request.method == 'POST':
    if 'file' in request.files:
      file = request.files['file']
      save_img(file)
      db.execute(
        "UPDATE books SET cover=? where id=?",
        (file.filename, book_id)
        )
      db.commit()
    return redirect(url_for('books.show', book_id=book_id)) 

  book = db.execute('SELECT * FROM books where id =?',book_id).fetchone()
  return render_template('books/upload.html', book=book)

@bp.route('/books/write',methods=['GET'])
def write():
  csv_str=""
  db = get_db()
  alldata = db.execute('SELECT * FROM books').fetchall()
  for data in alldata:
    csv_str += ",".join([data['title'],data['author'],data['cover']])
    csv_str += "\n"
  write_file("books.csv", csv_str)
  return render_template('books/write.html',str=csv_str)
