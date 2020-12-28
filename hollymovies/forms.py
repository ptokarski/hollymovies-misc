from datetime import date

from flask_wtf import FlaskForm
from flask_wtf.form import _Auto
from wtforms import (
    DateField, IntegerField, SelectField, StringField, ValidationError
)
from wtforms.validators import DataRequired, Length, NumberRange

from hollymovies.models import Genre


def capitalized_validator(form, field):
    if field.data[0].islower():
        raise ValidationError('Value must be capitalized.')


class PastDate:
    def __call__(self, form, field):
        if field.data >= date.today():
            raise ValidationError('Only past dates allowed here.')


class MovieForm(FlaskForm):

    def __init__(self, formdata=_Auto, **kwargs):
        super().__init__(formdata=formdata, **kwargs)
        self.genre.choices = Genre.query.with_entities(Genre.id, Genre.name)

    title = StringField(
        validators=[DataRequired(), Length(max=128), capitalized_validator]
    )
    rating = IntegerField(validators=[NumberRange(min=0, max=10)])
    genre = SelectField(validators=[DataRequired()])
    released = DateField(validators=[DataRequired(), PastDate()])
    description = StringField()

    def validate_rating(form, field):
        if form.genre.data != '9':  # id of comedy is 9
            return
        if field.data < 6:
            return
        raise ValidationError("Comedies aren't so good to be rated over 5.")
