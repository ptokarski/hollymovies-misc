from flask import Blueprint, render_template
from flask.views import MethodView

from hollymovies.models import Movie

main_blueprint = Blueprint('main', __name__)


class MovieListView(MethodView):
    def get(self):
        return render_template('movies.html', movies=Movie.query)


main_blueprint.add_url_rule('/', view_func=MovieListView.as_view('index'))
