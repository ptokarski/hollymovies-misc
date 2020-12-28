from flask_wtf import FlaskForm
from flask_wtf.form import _Auto
from wtforms import DateField, IntegerField, SelectField, StringField

from hollymovies.models import Genre


class MovieForm(FlaskForm):

    def __init__(self, formdata=_Auto, **kwargs):
        super().__init__(formdata=formdata, **kwargs)
        self.genre.choices = Genre.query.with_entities(Genre.id, Genre.name)

    title = StringField()
    rating = IntegerField()
    genre = SelectField(_name='genre_id')
    released = DateField()
    description = StringField()
