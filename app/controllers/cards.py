from flask import render_template, request, redirect, url_for
from app import app
from app.models.cards import CardsModel
import os
from pprint import pprint

app.config["UPLOAD_FOLDER"] = "./app/static"

class Cards:
    def index() -> str:
        lutadores = CardsModel.listar_todos()
        return render_template('cards/index.html', lutadores=lutadores)

    def novo() -> str:
        return render_template('cards/novo.html')

    def salvar() -> str:
        foto = request.files["foto"]
        data = {
            'nome': request.form['nome'],
            'idade': request.form['idade'],
            'forca': request.form['forca'],
            'foto': foto.filename
        }
        
        if CardsModel.salvar(data):
            path = os.path.join(app.config["UPLOAD_FOLDER"], foto.filename)
            foto.save(path)
            return redirect(url_for('index'))
        return 'erro ao salvar'

    def editar(id) -> str:
        lutador = CardsModel.listar_um(id)
        return render_template('cards/editar.html', lutador=lutador)

    def atualizar(id) -> str:
        foto = request.files["foto"]
        
        data = {
            'nome': request.form['nome'],
            'idade': request.form['idade'],
            'forca': request.form['forca'],
            'foto': foto.filename
        }

        if CardsModel.atualizar(id, data):
            return redirect(url_for('index'))

        return 'houve um erro'
    
    def deletar(id) -> str:
        if CardsModel.deletar(id):
            return redirect(url_for('index'))

        return 'houve um erro'
