from flask import Blueprint, redirect, render_template

from hollymovies import models
from hollymovies.forms import MovieForm

main_blueprint = Blueprint('main', __name__)


@main_blueprint.route('/')
def movies():
    return render_template('movies.html', movies=models.Movie.query)


@main_blueprint.route('/movie/create', methods=['GET', 'POST'])
def movie_create():
    form = MovieForm()
    if not form.validate_on_submit():
        return render_template('movie_form.html', form=form)
    movie = models.Movie(
        title=form.title.data,
        genre_id=int(form.genre.data),
        rating=form.rating.data,
        released=form.released.data,
        description=form.description.data
    )
    with models.session() as session:
        session.add(movie)
    return redirect('/')
