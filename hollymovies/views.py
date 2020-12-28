from flask import Blueprint, redirect, render_template, url_for
from flask_wtf import FlaskForm

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
    return redirect(url_for('main.movies'))


@main_blueprint.route('/movie/update/<movie_id>', methods=['GET', 'POST'])
def movie_update(movie_id):
    movie = models.Movie.query.get(movie_id)
    form = MovieForm(obj=movie)
    if not form.validate_on_submit():
        return render_template('movie_form.html', form=form)
    movie.title = form.title.data
    movie.genre_id = int(form.genre.data)
    movie.rating = form.rating.data
    movie.released = form.released.data
    movie.description = form.description.data
    with models.session() as session:
        session.add(movie)
    return redirect(url_for('main.movies'))


@main_blueprint.route('/movie/delete/<movie_id>', methods=['GET', 'POST'])
def movie_delete(movie_id):
    movie = models.Movie.query.get(movie_id)
    form = FlaskForm()
    if not form.validate_on_submit():
        context = {'form': form, 'title': movie.title}
        return render_template('movie_delete.html', **context)
    with models.session() as session:
        session.delete(movie)
    return redirect(url_for('main.movies'))
