from flask_sqlalchemy import *
from app import db

class Found(db.Model):
	__tablename__='found'
	id=db.Column(db.Integer,autoincrement=True,primary_key=True)
	fquery=db.Column(db.String(100))
	email=db.Column(db.String(255),db.ForeignKey('users.email'))

	def __init__(self,fquery,email):
		self.fquery=fquery
		self.email=email

	def to_dict(self):
		return {
                        'id':self.id,
                        'fquery':self.fquery,
                        'email':self.email,
		}

	def __repr__(self):
        	return "Query <%s> found" % (self.fquery)

