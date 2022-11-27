from flask import Blueprint, render_template, redirect, request, url_for, session
from entities.user import User


auth = Blueprint("auth", __name__, url_prefix="/auth")

superuser = User(username="teste", password="1234")


@auth.route("/login", methods=["POST", "GET"])
def login():
    parameters_template = {"title": "Login"}
    if request.method == 'post' or request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]

        if username and password and username == superuser.username and password == superuser.password:
            session["username"] = username
            return redirect(url_for('main.index'), code=200)
        
        parameters_template.update({"error": "Invalid credentials"})
    
    return render_template('auth/login.html', **parameters_template)

@auth.route("/logout", methods=["GET"])
def logout():
    session["username"] = None
    return redirect(url_for('main.index'))