from flask import Blueprint, render_template

main = Blueprint("main", __name__)

@main.route("/", methods=["GET"])
def index():
    username = None
    return render_template('index.html', username=username or "Guest")