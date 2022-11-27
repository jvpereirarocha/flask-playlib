from flask import Flask
from routes.main import main as main_bp
from routes.games import games as games_bp
from routes.auth import auth as auth_bp

app = Flask(__name__)
app.register_blueprint(auth_bp)
app.register_blueprint(main_bp)
app.register_blueprint(games_bp)

if __name__ == "__main__":
    app.run(debug=True)