from flask import Flask,request
from database_module import insert,create_me
app=Flask(__name__)
@app.route('/')
def homepage():
	return "<a href='/create'>Create database here</a>"
@app.route('/create')
def create():
	try:
		create_me()
		return "database created nigga"
	except:
		return "table already exist"
@app.route('/insert',methods=['POST'])
def insert_data():
	name=request.form['name']
	age=request.form['age']
	insert(name,age)
	return f'{str(name)} of age {age} inserteds'
