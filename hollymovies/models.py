from contextlib import contextmanager

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

ModelBase = declarative_base()


class Genre(ModelBase):
    __tablename__ = 'genre'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)


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
