from flask_sqlalchemy import *
from app import *

class Lost(db.Model):
	__tablename__='lost'
	id=db.Column(db.Integer,primary_key=True,autoincrement=True)
	lquery=db.Column(db.String(100))
	email=db.Column(db.String(255),db.ForeignKey('users.email'))

	def __init__(self,query,email):
		self.lquery=lquery
		self.email=email

	def to_dict(self):
		return {
                        'id':self.id,
                        'lquery':self.lquery,
                        'email':self.email,
		}


	def __repr__(self):
		return "Query %s added to user" % (self.lquery)


