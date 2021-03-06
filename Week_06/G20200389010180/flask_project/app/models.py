from sqlalchemy import Column, Integer, String, Float
from flask_sqlalchemy import SQLAlchemy
from app import db

class Douban(db.Model):
    __tablename__ = 'douban'

    id = db.Column(db.Integer, primary_key=True)
    n_star = db.Column(db.Integer)
    short = db.Column(db.String(255))
    sentiment = db.Column(db.Float)