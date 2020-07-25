from flask import Flask, jsonify, request
from flask_cors import CORS


DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

BOOKS = [
    {
        'title': 'The Witcher: Blood of Elves',
        'author': 'Andrzej Sapkowski',
        'rating': 94
    },
    {
        'title': 'The Witcher: Time of Contempt',
        'author': 'Andrzej Sapkowski',
        'rating': 98
    },
    {
        'title': 'The Witcher: Baptism of Fire',
        'author': 'Andrzej Sapkowski',
        'rating': 95
    },
    {
        'title': 'The Witcher: The Tower of the Swallow',
        'author': 'Andrzej Sapkowski',
        'rating': 94
    },
    {
        'title': 'The Witcher: Lady of the Lake',
        'author': 'Andrzej Sapkowski',
        'rating': 92
    },
    {
        'title': 'The Witcher: The Last Wish',
        'author': 'Andrzej Sapkowski',
        'rating': 93
    },
    {
        'title': 'The Witcher: Season of Storms',
        'author': 'Andrzej Sapkowski',
        'rating': 98
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
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'rating': post_data.get('rating')
        })
        response_obj['message'] = 'Title added'
    else:
        response_obj['books'] = BOOKS
    return jsonify(response_obj)


if __name__ == "__main__":
    app.run()
