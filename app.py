from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid


DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

BOOKS = [
    {
        'id': uuid.uuid4().hex,
        'title': 'The Witcher: Blood of Elves',
        'author': 'Andrzej Sapkowski',
        'rating': 94,
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'The Witcher: Time of Contempt',
        'author': 'Andrzej Sapkowski',
        'rating': 98,
        'read': False
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'The Witcher: Baptism of Fire',
        'author': 'Andrzej Sapkowski',
        'rating': 95,
        'read': False
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'The Witcher: The Tower of the Swallow',
        'author': 'Andrzej Sapkowski',
        'rating': 94,
        'read': False
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'The Witcher: Lady of the Lake',
        'author': 'Andrzej Sapkowski',
        'rating': 92,
        'read': False
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'The Witcher: The Last Wish',
        'author': 'Andrzej Sapkowski',
        'rating': 93,
        'read': False
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'The Witcher: Season of Storms',
        'author': 'Andrzej Sapkowski',
        'rating': 98,
        'read': False
    },
]

# enable cors
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/books', methods=['GET', 'POST'])
def all_books():
    response_obj = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'rating': post_data.get('rating'),
            'read': post_data.get('read')
        })
        response_obj['message'] = 'Title added'
    else:
        response_obj['books'] = BOOKS
    return jsonify(response_obj)


@app.route('/books/<book_id>', methods=['PUT', 'DELETE'])
def single_book(book_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_book(book_id)
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'rating': post_data.get('rating'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book updated!'
    if request.method == 'DELETE':
        remove_book(book_id)
        response_object['message'] = 'Book removed!'
    return jsonify(response_object)


def remove_book(book_id):
    for book in BOOKS:
        if book['id'] == book_id:
            BOOKS.remove(book)
            return True
    return False


if __name__ == "__main__":
    app.run()
