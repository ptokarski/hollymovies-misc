from contextlib import contextmanager
from datetime import datetime

from sqlalchemy import (
    Column, Date, DateTime, ForeignKey, Integer, String, create_engine
)
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import relationship, sessionmaker

models_registry = {}
ModelBase = declarative_base(class_registry=models_registry)


class Genre(ModelBase):
    __tablename__ = 'genre'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    movies = relationship('Movie', back_populates='genre')


class Movie(ModelBase):
    __tablename__ = 'movie'
    id = Column(Integer, primary_key=True)
    title = Column(String(length=128), nullable=False)
    genre_id = Column(Integer, ForeignKey('genre.id'), nullable=False)
    genre = relationship('Genre', back_populates='movies')
    rating = Column(Integer, nullable=False)
    released = Column(Date, nullable=False)
    description = Column(String)
    created = Column(DateTime, default=datetime.utcnow)


def all_models():
    for model in models_registry.values():
        if isinstance(model, DeclarativeMeta):
            yield model


ENGINE = create_engine('sqlite:///db.sqlite3')
Session = sessionmaker(bind=ENGINE)


@contextmanager
def session():
    result = Session()
    try:
        yield result
        result.commit()
    except Exception:
        result.rollback()
        raise
    finally:
        result.close()
