from flask import Flask,request,jsonify
import requests
from bs4 import BeautifulSoup
app= Flask(__name__)
def catch_all(path):
    return Response("<h1>Flask on Now</h1><p>You visited: /%s</p>" % (path), mimetype="text/html")
@app.route('/')
def nulljson():
	q=request.args['q']
	url="https://vidstreaming.io/"+q
	html=requests.get(url).text
	newlink=BeautifulSoup(html,'html.parser').iframe["src"]
	notstripped=requests.get("https:"+newlink).contents
	response=jsonify({"if":notstripped})
	response.headers.add('Access-Control-Allow-Origin', '*')
	response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
	response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
	return response
