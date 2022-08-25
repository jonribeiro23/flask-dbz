from app import app
from app.controllers.cards import Cards

@app.route('/')
def index() -> str:
    return Cards.index()

@app.route('/novo')
def novo() -> str:
    return Cards.novo()

@app.route('/salvar', methods=['POST'])
def salvar() -> str:
    return Cards.salvar()

@app.route('/editar/<string:id>')
def editar(id) -> str:
    return Cards.editar(id)

@app.route('/atualizar/<string:id>', methods=['POST'])
def atualizar(id) -> str:
    return Cards.atualizar(id)

@app.route('/deletar/<string:id>')
def deletar(id) ->str:
    return Cards.deletar(id)