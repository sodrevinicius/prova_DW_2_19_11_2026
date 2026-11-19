# Sistema de Salas - Prova Pratica Individual de DW2 (versao B)
#
# Este sistema JA EXECUTA. Leia o README.md: ele traz as regras da prova e
# os itens numerados que voce deve resolver.
#
# Como executar (na raiz do projeto, com o venv ativo):
#     python app.py

from flask import Flask
from werkzeug.security import generate_password_hash
from extensions import db
from controllers.sala_controller import sala_bp
from controllers.auth_controller import auth_bp
from controllers.api_controller import api_bp
from models.usuario import Usuario
from models.sala import Sala
from dao.usuario_dao import UsuarioDAO

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///prova.db"
app.secret_key = "dw2-prova-pratica"

db.init_app(app)

# Tres Blueprints, tres papeis:
#   sala_bp  -> paginas
#   auth_bp  -> entrada, cadastro de conta e saida
#   api_bp   -> dados em JSON
app.register_blueprint(sala_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(api_bp)

app.app_context().push()


# Cria as tabelas e, se o banco estiver vazio, a conta inicial e alguns
# registros de exemplo. NAO ALTERE esta funcao.
def preparar_banco():
    db.create_all()

    if UsuarioDAO.contar() == 0:
        conta = Usuario(
            nome="Coordenacao",
            email="coordenacao@fatec.local",
            senha_hash=generate_password_hash("prova123")
        )
        db.session.add(conta)
        db.session.add(Sala(nome="Laboratorio 1", bloco="Bloco A", capacidade=30))
        db.session.add(Sala(nome="Auditorio", bloco="Bloco B", capacidade=120))
        db.session.add(Sala(nome="Sala 12", bloco="Bloco A", capacidade=40))
        db.session.commit()


if __name__ == "__main__":
    preparar_banco()
    app.run(debug=True)
