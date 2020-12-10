from contextlib import contextmanager

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker

models_registry = {}
ModelBase = declarative_base(class_registry=models_registry)


class Genre(ModelBase):
    __tablename__ = 'genre'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)


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
