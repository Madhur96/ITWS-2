from flask import *
from app import *
from app.lost.models import *
from app.found.models import *
from flask_cors import *
from app.user.models import *

mod_found = Blueprint('found', __name__)
CORS(mod_found)

@mod_found.route('/found', methods=['GET'])
def get_all_found():
	data=Found.query.all()
	lis={'found':[]}
	for i in data:
	#	dic={}		
	#	dic["fquery"]=i.fquery
	#	dic["email"]=i.email	
		dic=i.to_dict()
		lis['found'].append(dic)
	return jsonify(lis)

@mod_found.route('/addFound', methods=['POST'])
def addFound():
	fquery=request.form['fquery']
	email=request.form['email']
	try:
		f=Found(fquery,email)
		db.session.add(f)
		db.session.commit()
		return 'Query added '
	except:
		return make_response("Details not valid",404,none)

if __name__ == '__main__':
	app.run(debug=True)

