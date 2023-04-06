from flask import Flask, request, jsonify
import json
import sqlite3
import logging

logging.getLogger('PIL').setLevel(logging.INFO)

app = Flask(__name__)

def databaseConnect():
    conn = None
    try:
        conn = sqlite3.connect('books.sqlite')
    except Exception as e:
        logging.info(f"Cannot make the connection: {e}")
    return conn        

@app.route('/books',methods=['GET', 'POST'])
def books():
    
    conn = databaseConnect()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor = conn.execute("SELECT * FROM books")
        books = [dict(id=row[0], author=row[1], title=row[2], pages=row[3]) for row in cursor.fetchall()]
        if books is not None:
            return jsonify(books)

    if request.method == 'POST':
        new_author = request.form['author']
        new_title = request.form['title']
        new_pg_num = request.form['pages']

        sql = """ INSERT INTO BOOKS (author, title, pages) VALUES (?,?,?)"""

        cursor = cursor.execute(sql, (new_author,new_title,new_pg_num))
        conn.commit()
        return f"Book with the id: {cursor.lastrowid} created successfully", 201

@app.route("/book/<int:id>",methods=['GET','PUT','DELETE'])
def singleBook(id):
    conn = databaseConnect()
    cursor = conn.cursor()
    book = None
    if request.method == "GET":
        cursor.execute("SELECT * FROM books WHERE id=?", (id,))
        rows = cursor.fetchall()
        for i in rows:
            book = i
        if book is not None:
            return jsonify(book), 200
        else:
            return "Something went wrong", 404

    if request.method == "PUT":
        sql = """ UPDATE books SET title=?, author=?, pages=? WHERE id=? """
        
        author = request.form['author']
        title = request.form['title']
        pages = request.form['pages']
        update_book = {'id':id, 'author':author, 'title':title, 'pages':pages}
        
        conn.execute(sql, (title, author, pages, id))
        conn.commit()
        return jsonify(update_book)

    if request.method == 'DELETE':
        sql = """ DELETE FROM books WHERE id=? """
        conn.execute(sql, (id,))
        conn.commit()
        return f"The book with id {id} has been deleted", 200    


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)