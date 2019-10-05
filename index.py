from flask import Flask,request,jsonify
from bs4 import BeautifulSoup as bs
import requests
app= Flask(__name__)
def catch_all(path):
    return Response("<h1>Flask on Now</h1><p>Fuck you , you cant access: /%s</p>" % (path), mimetype="text/html")
@app.route('/')
def nulljson():

	elist=[]
	c={}
	gc=request.args['g']
	url="https://vidstreaming.io/videos/"+gc
	data=requests.get(url).text
	soup=bs(data,'html.parser')
	allepisodes=soup.find('div',{'class':"video-info-left"}).find_all('li',{'class':"video-block"})
	for episodes in allepisodes:
		elist.append({episodes.find('div',{'class':"name"}).text:episodes.a['href']})
	elist.reverse()
	response=jsonify({"data":elist})
	response.headers.add('Access-Control-Allow-Origin', '*')
	response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
	response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
	return response
@app.route('/anime/<string:name>',methods=['POST'])
def findallepisode():
	pass
