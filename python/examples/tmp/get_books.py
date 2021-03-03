# Se importa la clase flask para poder iniciar el servidor.
from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route('/books', methods=['GET'])
def getBooks(book_id):
    
    books = {
        '1': {'name':'La Iliada', 'id':'1', 'author':'Anonymous'},
        '2': {'name':'La Odisea', 'id':'2', 'author':'Anonymous'},
        '3': {'name':'La Estampida', 'id':'3', 'author':'Anonymous'}
        }
        
    data = json.dumps(books)
    print(data)
    return data

@app.route('/')
def index():
    return 'Bienvenidos'

if __name__ == '__main__':
    app.run(debug=True)
