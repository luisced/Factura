from facturacion import db
from dataclasses import dataclass
from datetime import datetime


@dataclass
class User(db.Model):
    '''User model for storing user related details'''
    __tablename__ = 'User'
    id: int = db.Column(db.Integer, primary_key=True,
                        autoincrement=True, nullable=False)
    email: str = db.Column(db.String(120), unique=True, nullable=False)
    password: str = db.Column(db.String(60), nullable=False)
    status: bool = db.Column(db.Boolean, nullable=False, default=True)
    creation_date: str = db.Column(
        db.DateTime, nullable=False, default=datetime.now)
    last_update: str = db.Column(
        db.TIMESTAMP, nullable=False, default=datetime.now, onupdate=datetime.now)

    def __str__(self) -> str:
        return f'User({", ".join([f"{column.name}:{getattr(self, column.name)}" for column in self.__table__.columns])})'
