from datetime import datetime
from app.src import db
from dataclasses import dataclass


@dataclass
class UserModel(db.Model):
    __tablename__ = "users"
    id: int = db.Column(db.Integer, primary_key=True)
    registered_on: datetime = db.Column(db.DateTime, nullable=False)
    email: str = db.Column(db.String(255), unique=True, nullable=True)
    phone_no: int = db.Column(db.String(80), unique=True, nullable=True)
    username: str = db.Column(db.String(80), nullable=False, unique=True)
    password:str = db.Column(db.String(255), nullable=False)
    
    @classmethod
    def create(cls, **kw):
        obj = cls(**kw)
        db.session.add(obj)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username: str) -> "UserModel":
        return cls.query.filter_by(username=username).first()
