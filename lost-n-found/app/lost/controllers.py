from flask import *
from app import *
from flask_cors import *
from app.user.models import *
from app.lost.models import *
mod_lost=Blueprint('lost',__name__)
CORS(mod_lost)

@mod_lost.route('/')
def welcome():
    return 'Hello'
    
@mod_lost.route('/lost',methods=['GET'])
def get_all_lost():
	lo=Lost.query.all()
	llist={'lost':[]}
	found=Found.query.all()
	for i in lo:
	#	ldict={}
	#	ldict["lquery"]=i.lquery
	#	ldict["email"]=i.email
		ldict=i.to_dict()
		p=[]
		for j in found:
		    if (str(j.fquery)==str(i.lquery)):
		        p.append(j.email)
		ldict['found']=p
		llist['lost'].append(ldict)

	return jsonify(llist)
	
@mod_lost.route('/addLost',methods=['POST'])
def addLost():
	lquery=request.form['lquery']
	email=request.form['email']

	try:
		l=Lost(lquery,email)
		db.session.add(l)
		db.session.commit()
		return "Query added"
	
	except:
		return make_response("Details not valid",404,none)

if __name__ == '__main__':
	app.run(debug=True)




