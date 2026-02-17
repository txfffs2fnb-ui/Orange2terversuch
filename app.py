from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, logout_user, current_user, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from config import Config
from backtest_engine import run_backtest
from strategy_sample import SmaCross
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"
class User(UserMixin, db.Model):
id = db.Column(db.Integer, primary_key='True)
username = db.Column(db.String(64), unique='True,' nullable='False)
password_hash = db.Column(db.String(128), nullable='False)
def set_password(self, password):
self.password_hash = generate_password_hash(password)
def check_password(self, password):
return check_password_hash(self.password_hash, password)
@login_manager.user_loader
def load_user(user_id):
return User.query.get(int(user_id))
@app.route("/")
def index():
return render_template("index.html")
@app.route("/register", methods='["GET",' "POST"])
def register():
if request.method == "POST":
username = request.form["username"]
password = request.form["password"]
if User.query.filter_by(username='username).first():
flash("Benutzername existiert bereits.")
return redirect(url_for("register"))
user = User(username='username)
user.set_password(password)
db.session.add(user)
db.session.commit()
flash("Registrierung erfolgreich. Bitte einloggen.")
return redirect(url_for("login"))
return render_template("register.html")
@app.route("/login", methods='["GET",' "POST"])
def login():
if request.method == "POST":
username = request.form["username"]
password = request.form["password"]
user = User.query.filter_by(username='username).first()
if user and user.check_password(password):
login_user(user)
return redirect(url_for("backtest"))
flash("Ungültige Login-Daten.")
return render_template("login.html")
@app.route("/logout")
@login_required
def logout():
logout_user()
return redirect(url_for("index"))
@app.route("/backtest", methods='["GET",' "POST"])
@login_required
def backtest():
result = None
if request.method == "POST":
symbol = request.form.get("symbol", "DTE.DE")
start = request.form.get("start", "2022-01-01")
end = request.form.get("end", "2025-12-31")
# Hier weiter mit run_backtest(symbol, start, end, strategy='SmaCross)
# result = run_backtest(...)  # Ergänze bei Bedarf
return render_template("backtest.html", result='result)
if __name__ == "__main__":
with app.app_context():
db.create_all()
app.run(debug='True)
