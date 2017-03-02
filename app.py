from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)

db_books = [
    {
        'id': 1,
        'title': 'Python Cookbook',
        'tags': ['Python', 'Algorithms', 'Development'],
        'authors': ['David Beazley', 'Brian K. Jones'],
        'publishing': ["O'Reilly", 'Novatec']
    },
    {
        'id': 2,
        'title': 'Flask Cookbook',
        'tags': ['Python', 'Algorithms', 'Development', 'Flask'],
        'authors': ['Shalabh Aggarwal'],
        'publishing': 'PACKT'
    },
    {
        'id': 3,
        'title': 'Flask Web Development',
        'tags': ['Python', 'Algorithms', 'Development', 'Flask'],
        'authors': ['Miguel Grinberg'],
        'publishing': "O'Reilly"
    },
]


@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad Request'}), 400)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/v1/books', methods=['GET'])
def get_books():
    books = {'total': len(db_books), 'objects': db_books}
    return jsonify(books)


@app.route('/v1/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = [book for book in db_books if book['id'] == book_id]
    if len(book) == 0:
        abort(404)
    return jsonify(book[0])


@app.route('/v1/books', methods=['POST'])
def create_book():
    if not request.json or ('title' not in request.json):
        abort(400)
    book = {
        'id': db_books[-1]['id'] + 1,
        'title': request.json['title'],
        'tags': request.json['tags'],
        'authors': request.json['authors'],
        'publishing': request.json['publishing'],
    }
    db_books.append(book)
    return jsonify(book), 201


@app.route('/v1/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = [book for book in db_books if book['id'] == book_id]

    # basic validations
    if len(book) == 0:
        abort(404)
    if not request.json:
        abort(400)

    # data validations
    if ('title' in request.json and not isinstance(request.json['title'], str)):
        abort(400)
    if ('publishing' in request.json and not isinstance(request.json['publishing'], str)):
        abort(400)

    if ('tags' in request.json and not isinstance(request.json['tags'], list)):
        abort(400)
    if ('authors' in request.json and not isinstance(request.json['authors'], list)):
        abort(400)

    book[0].update(**request.json)
    return jsonify(book[0])


@app.route('/v1/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = [book for book in db_books if book['id'] == book_id]
    if len(book) == 0:
        abort(404)
    db_books.remove(book[0])
    return ('', 200)

if __name__ == '__main__':
    app.run(debug=True)
