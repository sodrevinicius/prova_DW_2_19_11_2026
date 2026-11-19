# Model - entidade Sala.

from extensions import db


class Sala(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    bloco = db.Column(db.String(120))
    capacidade = db.Column(db.Integer)

    # O objeto se descreve como dicionario, para as rotas que respondem JSON.
    def para_dicionario(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "bloco": self.bloco,
            "capacidade": self.capacidade
        }
