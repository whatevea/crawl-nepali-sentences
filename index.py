from flask import Flask,request
import requests
app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
	if request.method=='POST':
		headers=request.form
		url=request.args['url']
		url="https://"+url.replace('^','/')
		response= requests.get(url,headers=headers).text
		response.headers.add('Access-Control-Allow-Origin', '*')
		response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
		response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
	else:
		url=request.args['url']
		url="https://"+url.replace('^','/')
		response=requests.get(url).text
		response.headers.add('Access-Control-Allow-Origin', '*')
		response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
		response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
