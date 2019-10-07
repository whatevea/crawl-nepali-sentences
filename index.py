from flask import Flask,request,jsonify
import requests
app= Flask(__name__)
def catch_all(path):
    return Response("<h1>Flask on Now</h1><p>You visited: /%s</p>" % (path), mimetype="text/html")
@app.route('/')
def nulljson():
	q=request.args['q']
	url="https://vidstreaming.io/"+q
	html=requests.get(url).text
	iframe=html.find('<iframe')
	iframe2=html.find('>',iframe)+1
	notstripped=html[iframe:iframe2]
	titlel=notstripped.find(r'&title')
	nextamp=notstripped.find(r'&',titlel)
	stpd=notstripped[titlel:nextamp]
	stripped=notstripped.split(r'&type')[0]+'" allowfullscreen="true"  height="600px" width="900px" frameborder="0" marginwidth="0" marginheight="0" scrolling="no"></iframe>'
	return {"iframe":stripped}
