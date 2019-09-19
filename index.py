from flask import Flask,request,jsonify
from bs4 import BeautifulSoup as bs
import requests
app= Flask(__name__)
def catch_all(path):
    return Response("<h1>Flask on Now</h1><p>You visited: /%s</p>" % (path), mimetype="text/html")
@app.route('/')
def nulljson():

	epsiodelist=[]
	c={}
	gc=request.args['g']
	url="https://www.gogoanime1.com/watch/"+gc
	resp=requests.get(url).text
	soup=bs(resp,'html.parser')
	soup=soup.find_all('div',{'class':'ci-ct tnContent'})[1]
	total=soup.find_all('li')
	for items in total:
		c={items.a['href']:items.a['href'].rsplit('/',1)[1]}
		epsiodelist.append(c)
	response=jsonify({"data":epsiodelist})
	response.headers.add('Access-Control-Allow-Origin', '*')
	response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
	response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
	return response
@app.route('/anime/<string:name>',methods=['POST'])
def findallepisode():
	pass
