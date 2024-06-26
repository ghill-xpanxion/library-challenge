from flask import Flask, jsonify
from test_data import books

app = Flask(__name__)


# route for getting books by id
@app.route('/books/<int:id>', methods=['GET'])
def get_book_by_id(id):
    book = next((book for book in books if book['id'] == id), None)
    if book is not None:
        return jsonify(book)
    else:
        return jsonify({"error": "Book not found"}), 404

if __name__ == "__main__":
    app.run()