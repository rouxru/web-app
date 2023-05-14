"""Database models."""
from flask_login import UserMixin


from app import db


class Data(UserMixin, db.Model):
    """User account model."""

    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key=True)
    Type = db.Column(db.String(100), nullable=False, unique=False)
    Model = db.Column(db.String(100), nullable=False, unique=False)
    Characteristics = db.Column(db.String(100), nullable=False, unique=False)
    staff = db.Column(db.String(100), nullable=False, unique=False)
    Location = db.Column(db.String(100), nullable=False, unique=False)
    Status = db.Column(db.String(100), nullable=False, unique=False)
    MAC = db.Column(db.String(100), nullable=False, unique=False)
    Name = db.Column(db.String(100), nullable=False, unique=False)
    Inventory = db.Column(db.String(100), nullable=False, unique=False)
    Graphics = db.Column(db.String(100), nullable=False, unique=False)
    Comments = db.Column(db.String(100), nullable=False, unique=False)
    Serial = db.Column(db.String(100), nullable=False, unique=False)
    username = db.Column(db.String(100), nullable=False, unique=False)
    warranty = db.Column(db.String(100), nullable=False, unique=False)
    Order = db.Column(db.String(100), nullable=False, unique=False)
