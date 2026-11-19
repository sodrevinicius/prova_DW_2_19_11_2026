# DAO - concentra o acesso aos dados de Sala.

from extensions import db
from models.sala import Sala


class SalaDAO:

    # CREATE
    @staticmethod
    def salvar(sala):
        db.session.add(sala)

    # READ (todos)
    @staticmethod
    def listar():
        return Sala.query.all()

    # READ (um) - devolve o objeto ou None
    @staticmethod
    def buscar_por_id(id):
        return Sala.query.get(id)

    # UPDATE
    @staticmethod
    def atualizar(sala, nome, bloco, capacidade):
        sala.nome = nome
        sala.bloco = bloco
        sala.capacidade = capacidade
        db.session.commit()

    # DELETE
    @staticmethod
    def excluir(sala):
        db.session.delete(sala)
        db.session.commit()
