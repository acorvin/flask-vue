from flask import Flask, jsonify
from flask_cors import CORS


DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

BOOKS = [
    {
        'Title': 'The Witcher: Blood of Elves',
        'Author': 'Andrzej Sapkowski',
        'Rating': 94
    },
    {
        'Title': 'The Witcher: Time of Contempt',
        'Author': 'Andrzej Sapkowski',
        'Rating': 98
    },
    {
        'Title': 'The Witcher: Baptism of Fire',
        'Author': 'Andrzej Sapkowski',
        'Rating': 95
    },
    {
        'Title': 'The Witcher: The Tower of the Swallow',
        'Author': 'Andrzej Sapkowski',
        'Rating': 94
    },
    {
        'Title': 'The Witcher: Lady of the Lake',
        'Author': 'Andrzej Sapkowski',
        'Rating': 92
    },
    {
        'Title': 'The Witcher: The Last Wish',
        'Author': 'Andrzej Sapkowski',
        'Rating': 93
    },
    {
        'Title': 'The Witcher: Season of Storms',
        'Author': 'Andrzej Sapkowski',
        'Rating': 98
    },
]

# enable cors
CORS(app, resources={r'/*': {'origins': '*'}})

# sanity check route
# @app.route('/ping', methods=['GET'])
# def ping_pong():
#     return jsonify('pong!')


@app.route('/books', methods=['GET'])
def all_books():
    return jsonify({
        'status': 'success',
        'books': BOOKS
    })


if __name__ == "__main__":
    app.run()
