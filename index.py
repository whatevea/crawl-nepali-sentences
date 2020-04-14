from flask import Flask,request,jsonify
from bs4 import BeautifulSoup,SoupStrainer
import requests
app= Flask(__name__)
def catch_all(path):
    return Response("<h1>Flask on Now</h1><p>Fuck you , you cant access: /%s</p>" % (path), mimetype="text/html")
@app.route('/')
def nulljson():
	url="https://vidstreaming.io/videos/"+request.args['url']
	html=requests.get(url).text
	openloadUrl="https"+(BeautifulSoup(html,'html.parser').iframe['src']).replace('streaming.php','load.php')
	response=jsonify({"openload":openloadUrl})
	response.headers.add('Access-Control-Allow-Origin', '*')
	response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
	response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
	return response
@app.route('/anime/<string:name>',methods=['POST'])
def findallepisode():
	pass
