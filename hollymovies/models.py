from contextlib import contextmanager
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import DeclarativeMeta

db = SQLAlchemy()


class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    movies = db.relationship('Movie', back_populates='genre')


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(length=128), nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'), nullable=False)
    genre = db.relationship('Genre', back_populates='movies')
    rating = db.Column(db.Integer, nullable=False)
    released = db.Column(db.Date, nullable=False)
    description = db.Column(db.String)
    created = db.Column(db.DateTime, default=datetime.utcnow)


def all_models():
    for model in db.Model._decl_class_registry.values():
        if isinstance(model, DeclarativeMeta):
            yield model


@contextmanager
def session():
    result = db.session()
    try:
        yield result
        result.commit()
    except Exception:
        result.rollback()
        raise
    finally:
        result.close()
