# DAO - acesso aos dados de usuario.

from extensions import db
from models.usuario import Usuario


class UsuarioDAO:

    @staticmethod
    def salvar(usuario):
        db.session.add(usuario)
        db.session.commit()

    @staticmethod
    def buscar_por_email(email):
        return Usuario.query.filter_by(email=email).first()

    @staticmethod
    def contar():
        return len(Usuario.query.all())
