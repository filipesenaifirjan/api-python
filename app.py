from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'O Senhor dos Anéis',
        'autor': 'J.R.R Tolkien'
    },
    {
        'id': 2,
        'titulo': 'Harry Potter',
        'autor': 'J.K howling'
    },
    {
        'id': 3,
        'titulo': 'Ja,es Clear',
        'autor': 'Habitos atonicos'
    },
]
#consultar
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

#consultar
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
      if  livro.get('id')  == id:
            return jsonify(livro)   


app.run(port=5000, host='localhost' ,debug=True)    