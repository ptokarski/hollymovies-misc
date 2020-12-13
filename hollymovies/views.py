from flask import Blueprint
from flask_generic_views import TemplateView

from hollymovies.models import Movie

main_blueprint = Blueprint('main', __name__)


class MovieListView(TemplateView):

    def get_context_data(self):
        result = super().get_context_data()
        result['movies'] = Movie.query
        return result

    template_name = 'movies.html'


main_blueprint.add_url_rule('/', view_func=MovieListView.as_view('index'))
