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
		return response
	else:
		url=request.args['url']
		url="https://"+url.replace('^','/')
		response=requests.get(url).text
		return response
