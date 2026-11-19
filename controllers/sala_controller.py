# Controller de PAGINAS - todas as rotas daqui respondem HTML ou
# redirecionamento.

from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask import session
from models.sala import Sala
from dao.sala_dao import SalaDAO

sala_bp = Blueprint("sala", __name__)


# ===== ITEM 5 ========================================================
# Hoje qualquer pessoa abre as paginas deste Blueprint sem entrar no
# sistema. Escreva aqui a protecao, em um ponto so.
# =====================================================================


# Listagem (GET) e cadastro (POST) na mesma rota
@sala_bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        sala = Sala(
            nome=request.form["nome"],
            bloco=request.form["bloco"],
            capacidade=request.form["capacidade"]
        )
        SalaDAO.salvar(sala)
        flash("Sala cadastrada.")
        return redirect(url_for("sala.index"))

    # ===== ITEM 3 ====================================================
    # Conte aqui, na SESSAO, quantas vezes esta pessoa abriu a listagem.
    # A chave deve se chamar "acessos". O template ja exibe o valor.
    # =================================================================

    return render_template("index.html", salas=SalaDAO.listar())


# Edicao - GET mostra o formulario preenchido
@sala_bp.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    sala = SalaDAO.buscar_por_id(id)

    # ===== ITEM 4 ====================================================
    # O formulario de edicao e enviado para esta rota por POST, mas nada
    # e gravado. Trate aqui o envio: grave a alteracao e volte a listagem.
    # =================================================================

    return render_template("editar.html", sala=sala)


# Exclusao
@sala_bp.route("/excluir/<int:id>", methods=["POST"])
def excluir(id):
    sala = SalaDAO.buscar_por_id(id)
    SalaDAO.excluir(sala)
    flash("Sala excluida.")
    return redirect(url_for("sala.index"))
