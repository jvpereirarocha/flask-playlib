from flask import Blueprint, render_template, request, redirect, url_for
from entities.play import Play

games = Blueprint("game", __name__, url_prefix="/games")


list_of_games = []

@games.route("/", methods=["GET"])
def fetch_all_games():
    return render_template('games/list.html', title='Jogos a listar', games=list_of_games)

@games.route("/new", methods=["POST", "GET"])
def create_new_game():
    if request.method == 'post' or request.method == 'POST':
        name = request.form["name"]
        category = request.form["category"]
        console = request.form["console"]
        new_game = Play(name, category, console)
        list_of_games.append(new_game)
        return redirect(url_for('game.fetch_all_games'), code=200)
    
    return render_template('games/new.html', title="Novo Jogo")