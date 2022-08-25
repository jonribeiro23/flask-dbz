from db import db
from bson import ObjectId

lutadores = db['lutadores']

class CardsModel:

    def salvar(dados):
        res = lutadores.insert_one(dados)
        if res.inserted_id:
            return True

        return False
        
    def listar_todos():
        return lutadores.find()

    def listar_um(id):
        return lutadores.find_one({'_id': ObjectId(id)})

    def atualizar(id, dados):
        res = lutadores.update_one(
            {'_id': ObjectId(id)}, 
            {'$set': dados}
            )
        return True

    def deletar(id):
        res = lutadores.delete_one({'_id': ObjectId(id)})
        return res.deleted_count > 0

