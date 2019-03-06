# coding=utf-8
from norwhale import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return "<User(username='%s', email='%s')>" % (self.username, self.email)

    @property
    def serialize(self):
        """return object data in easily serializeable format"""
        return {
            'username': self.username,
            'email': self.email
        }
    def serialize_multi(self):
        """return multipule data easily serializeable format"""
        return [item.serialize for item in self.serialize_multi]
