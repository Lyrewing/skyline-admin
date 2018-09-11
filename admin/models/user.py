from admin.models import Base, Session, engine
from sqlalchemy import Column, String, Integer
from admin.libs.md5 import md5
from sqlalchemy.orm import scoped_session


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(64), nullable=False, index=True)
    phone = Column(String(64), nullable=True, index=False)
    _password = Column('password', String(100))

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = md5(raw)

    @staticmethod
    def register_by_email(email, secret,phone):
        session = scoped_session(Session)
        user = User()
        user.email = email
        user.phone = phone
        user.password = secret
        try:
            session.add(user)
            session.commit()
        except Exception as err:
            print(err)

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.name)

    @staticmethod
    def verify(email: str, secret: str) -> bool:
        session = scoped_session(Session)
        user = session.query(User).filter(User.email == email).first()
        if user:
            password = md5(secret)
            password_db = user.password
            if password_db == password:
                return True
            else:
                return False
        else:
            return False

    @staticmethod
    def get_all_user():
        session = scoped_session(Session)
        user_objs = session.query(User).all()
        users = []
        for user in user_objs:
            users.append(user.dict())
        return users

    def dict(self):
        return {"id": self.id, "email": self.email, "phone": self.phone}


Base.metadata.create_all(engine)
