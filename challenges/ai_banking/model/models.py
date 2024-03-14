from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):

    __tablename__ = "accounts"

    email = Column(String(length=255), primary_key=True)
    password = Column(String(length=255))
    balance = Column(Integer())
    notes = Column(String(length=255))

    def __repr__(self):
        return f'User(email={self.email}, password={self.password}, balance={self.balance}, notes={self.notes})'

