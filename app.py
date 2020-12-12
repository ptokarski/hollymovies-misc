from flask import Flask
from flask_bootstrap import Bootstrap
from sqlalchemy.orm import scoped_session

from hollymovies.models import ModelBase, Session
from hollymovies.views import main_blueprint

db_session = scoped_session(Session)
ModelBase.query = db_session.query_property()

app = Flask(__name__)
app.register_blueprint(main_blueprint)
Bootstrap(app)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == "__main__":
    app.run()
