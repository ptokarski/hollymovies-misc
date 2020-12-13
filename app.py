from flask import Flask
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate

from hollymovies.models import db
from hollymovies.views import main_blueprint

app = Flask(__name__)
app.register_blueprint(main_blueprint)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
Migrate(app, db)
Bootstrap(app)


if __name__ == "__main__":
    app.run()
