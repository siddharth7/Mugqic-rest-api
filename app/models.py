from app import db


class User(db.Model):
    phonenumber = db.Column(db.String(120), index=True)
    name = db.Column(db.String(120), index=True, unique=True,primary_key=True)
    def __repr__(self):
        return '<User %r>' % (self.name)

    def __init__(self, phonenumber, name):
    	self.phonenumber = phonenumber
    	self.name = name

