from admin.models import Base, engine
from sqlalchemy import Column, String, Integer


class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False, index=True)
    author = Column(String(32), nullable=False, index=False)

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.name)


Base.metadata.create_all(engine)
