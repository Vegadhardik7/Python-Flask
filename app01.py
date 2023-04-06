from flask import Flask, request, jsonify

app = Flask(__name__)

books_list = [
    {
      "id": 1,
      "author": "J.K. Rowling",
      "title": "Harry Potter and the Sorcerer's Stone",
      "pages": 309
    },
    {
      "id": 2,
      "author": "J.R.R. Tolkien",
      "title": "The Lord of the Rings",
      "pages": 1178
    },
    {
      "id": 3,
      "author": "George R.R. Martin",
      "title": "A Game of Thrones",
      "pages": 694
    },
    {
      "id": 4,
      "author": "Suzanne Collins",
      "title": "The Hunger Games",
      "pages": 374
    },
    {
      "id": 5,
      "author": "J.D. Salinger",
      "title": "The Catcher in the Rye",
      "pages": 277
    },
    {
      "id": 6,
      "author": "Harper Lee",
      "title": "To Kill a Mockingbird",
      "pages": 281
    },
    {
      "id": 7,
      "author": "Stephenie Meyer",
      "title": "Twilight",
      "pages": 498
    },
    {
      "id": 8,
      "author": "John Green",
      "title": "The Fault in Our Stars",
      "pages": 313
    },
    {
      "id": 9,
      "author": "F. Scott Fitzgerald",
      "title": "The Great Gatsby",
      "pages": 180
    },
    {
      "id": 10,
      "author": "William Golding",
      "title": "Lord of the Flies",
      "pages": 208
    }
]


@app.route('/books',methods=['GET', 'POST'])
def books():
    if request.method == 'GET':
        if len(books_list) >0:
            return jsonify(books_list)
        else:
            "Nothing Found", 404

    if request.method == 'POST':
        new_author = request.form['author']
        new_title = request.form['title']
        new_pg_num = request.form['pages']
        new_id = books_list[-1]['id']+1

        new_obj = {'id':new_id, 'author':new_author, 'title':new_title, 'pages':new_pg_num}

        books_list.append(new_obj)
        return jsonify(books_list), 201
    

@app.route("/book/<int:id>",methods=['GET','PUT','DELETE'])
def singleBook(id):
    if request.method == "GET":
        for book in books_list:
            if book['id'] == id:
                return jsonify(book)
            pass

    if request.method == "PUT":
        for book in books_list:
            if book['id'] == id:
                book['author'] = request.form['author']
                book['title'] = request.form['title']
                book['pages'] = request.form['pages']
                update_book = new_obj = {'id':id, 'author':book['author'], 'title':book['title'], 'pages':book['pages']}
                return jsonify(update_book)

    if request.method == 'DELETE':
        for index, book in enumerate(books_list):
            if book['id'] == id:
                books_list.pop(index)
                return jsonify(books_list)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)