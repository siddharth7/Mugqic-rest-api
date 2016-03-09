from flask import render_template, flash, redirect, json, Response, request, session
import models
from app import app, db

@app.route('/')
@app.route('/index')
def index():
	return render_template('base.html',title='Data')

@app.route('/users', methods=['GET'])
def return_users():
	users=models.User.query.all()
	data_list=[]
	for user in users:
		data={}
		data['name']=user.name
		data['phone']=user.phonenumber
		data_list.append(data)
	js = json.dumps(data_list)
	resp = Response(js, status=200, mimetype='application/json')
	resp.headers['Link']='localhost:5000'
	return resp

@app.route('/users/<string:name>', methods=['GET'])
def return_user(name):
	user=models.User.query.filter_by(name=name).first()
	if user==None:
		data={}
		data['success']='false'
		data['error']='User not found'
		js= json.dumps(data)
		resp = Response(js, status=400, mimetype='application/json')
		resp.headers['Link']='localhost:5000'
		return resp
	else:
		data={}
		data['name']=user.name
		data['phone']=user.phonenumber
		data['success']='true'
		js= json.dumps(data)
		resp = Response(js, status=200, mimetype='application/json')
		resp.headers['Link']='localhost:5000'
		return resp

@app.route('/users/add', methods=['POST'])
def add_user():
	content = request.get_json(silent=True)
	if('name' in content and 'phone' in content):
		try:
			user = models.User(name=content['name'], phonenumber=content['phone'])
			db.session.add(user)
			db.session.commit()
			data={}
			data[content['name']]=content['phone']
			data['success']='true'
			js= json.dumps(data)
			resp = Response(js, status=201, mimetype='application/json')
			resp.headers['Link']='localhost:5000'
			return resp
		except:
			data={}
			data['error']='Already in Db'
			data['success']='false'
			js= json.dumps(data)
			resp = Response(js, status=501, mimetype='application/json')
			resp.headers['Link']='localhost:5000'
			return resp
	elif('name' not in content):
		data={}
		data['error']='Name not found'
		data['success']='false'
		js= json.dumps(data)
		resp = Response(js, status=501, mimetype='application/json')
		resp.headers['Link']='localhost:5000'
		return resp
	elif('phone' not in content):
		data={}
		data['error']='Phone Number not found'
		data['success']='false'
		js= json.dumps(data)
		resp = Response(js, status=501, mimetype='application/json')
		resp.headers['Link']='localhost:5000'
		return resp
	else:
		data={}
		data['error']='Name and Phone Number not found'
		data['success']='false'
		js= json.dumps(data)
		resp = Response(js, status=501, mimetype='application/json')
		resp.headers['Link']='localhost:5000'
		return resp

@app.route('/users/add', methods=['PUT'])
def add_user_todb():
	content = request.get_json(silent=True)
	if('name' in content and 'phone' in content):
		try:
			user = models.User(name=content['name'], phonenumber=content['phone'])
			db.session.add(user)
			db.session.commit()
			data={}
			data[content['name']]=content['phone']
			data['success']='true'
			js= json.dumps(data)
			resp = Response(js, status=201, mimetype='application/json')
			resp.headers['Link']='localhost:5000'
			return resp
		except:
			data={}
			data['error']='Already in Db'
			data['success']='false'
			js= json.dumps(data)
			resp = Response(js, status=501, mimetype='application/json')
			resp.headers['Link']='localhost:5000'
			return resp
	elif('name' not in content):
		data={}
		data['error']='Name not found'
		data['success']='false'
		js= json.dumps(data)
		resp = Response(js, status=501, mimetype='application/json')
		resp.headers['Link']='localhost:5000'
		return resp
	elif('phone' not in content):
		data={}
		data['error']='Phone Number not found'
		data['success']='false'
		js= json.dumps(data)
		resp = Response(js, status=501, mimetype='application/json')
		resp.headers['Link']='localhost:5000'
		return resp
	else:
		data={}
		data['error']='Name and Phone Number not found'
		data['success']='false'
		js= json.dumps(data)
		resp = Response(js, status=501, mimetype='application/json')
		resp.headers['Link']='localhost:5000'
		return resp



