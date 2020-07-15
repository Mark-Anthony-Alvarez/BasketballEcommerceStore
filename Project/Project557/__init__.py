from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)

# the above creates a variable for me to use SQLAlchemy within my project using db.
# app creates my web app with the speedy and light flask framework.


def create_app():
    app.debug = True
    app.secret_key = 'BetterSecretNeeded123'

    # set the app configuration data to project.sqlite as I name my database.
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.sqlite'

    # initialize db with flask app, A.K.A initializing SQLAlchemy with Flask
    db.init_app(app)

    bootstrap = Bootstrap(app)

    # importing modules here to avoid circular references, register blueprints of routes
    from . import views
    app.register_blueprint(views.bp)
    #from . import admin
    # app.register_blueprint(admin.bp) , I used this to import my data with admin.bp as shown in admin.py

    return app


@app.errorhandler(404)
# function which takes error as parameter
def not_found(e):
    return render_template("404.html")


@app.errorhandler(500)
def internal_error(e):
    return render_template("500.html")
