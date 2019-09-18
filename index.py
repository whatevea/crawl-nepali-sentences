from flask import Flask,Response
app= Flask(__name__)
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return Response("<h1>Flask on Now</h1><p>You visited: /%s</p>" % (path), mimetype="text/html")
@app.route('/')
def nulljson():
	return "NO request"
@app.route('/anime/<string:name>',methods=['POST'])
def findallepisode():
	pass
