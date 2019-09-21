from flask import Flask,request,jsonify
from bs4 import BeautifulSoup,SoupStrainer
import requests
app= Flask(__name__)
def catch_all(path):
    return Response("<h1>Flask on Now</h1><p>Fuck you , you cant access: /%s</p>" % (path), mimetype="text/html")
@app.route('/')
def nulljson():

	epsiodelist=[]
	c={}
	gc=request.args['g']
	url="https://www.gogoanime1.com/watch/"+gc
	resp=requests.get(url).text
	strainerobj=SoupStrainer('div',{'class':'ci-ct tnContent'})
	soup=BeautifulSoup(resp,'html.parser',parse_only=strainerobj)
	total=soup.find_all('div',{'class':'ci-ct tnContent'})[1].find_all('li')
	for items in total:
		link=items.a['href']
		newreq=requests.get(link).text
		# newbsobj=BeautifulSoup(newreq,'html.parser')
		secondstobj=SoupStrainer('a')
		ssoup=BeautifulSoup(newreq,'html.parser',parse_only=secondstobj)
		videolink=ssoup.find('a',text="Download")['href']
		c={items.a['href'].rsplit('/',1)[1]:videolink}
		# c={items.a['href']:items.a['href'].rsplit('/',1)[1]}
		epsiodelist.append(c)

	# epsiodelist=[dict(t) for t in {tuple(sorted(d.items())) for d in epsiodelist}] #filtering duplicates due to two 
	epsiodelist.reverse()
	response=jsonify({"data":epsiodelist})
	response.headers.add('Access-Control-Allow-Origin', '*')
	response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
	response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
	return response
@app.route('/anime/<string:name>',methods=['POST'])
def findallepisode():
	pass
