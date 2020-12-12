from flask import Blueprint, render_template

from hollymovies.models import Movie

main_blueprint = Blueprint('main', __name__)


@main_blueprint.route('/')
def movies():
    return render_template('movies.html', movies=Movie.query)
