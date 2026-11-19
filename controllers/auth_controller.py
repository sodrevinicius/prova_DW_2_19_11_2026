# Controller de autenticacao - entrar, criar conta e sair.
# Estas rotas ficam FORA da protecao: sem elas ninguem entraria.

from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask import session
from werkzeug.security import check_password_hash
from models.usuario import Usuario
from dao.usuario_dao import UsuarioDAO

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = UsuarioDAO.buscar_por_email(request.form["email"])

        if usuario and check_password_hash(usuario.senha_hash,
                                           request.form["senha"]):
            session["usuario_id"] = usuario.id
            session["usuario_nome"] = usuario.nome
            return redirect(url_for("sala.index"))

        flash("E-mail ou senha invalidos.")

    return render_template("login.html")


@auth_bp.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        if UsuarioDAO.buscar_por_email(request.form["email"]):
            flash("Ja existe uma conta com este e-mail.")
            return render_template("cadastro.html")

        usuario = Usuario(
            nome=request.form["nome"],
            email=request.form["email"],
            senha_hash=request.form["senha"]
        )
        UsuarioDAO.salvar(usuario)
        flash("Conta criada. Faca login para continuar.")
        return redirect(url_for("auth.login"))

    return render_template("cadastro.html")


@auth_bp.route("/sair", methods=["POST"])
def sair():
    session.clear()
    return redirect(url_for("auth.login"))
