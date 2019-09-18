from flask import Flask,request
app= Flask(__name__)
def catch_all(path):
    return Response("<h1>Flask on Now</h1><p>You visited: /%s</p>" % (path), mimetype="text/html")
@app.route('/')
def nulljson():
	gc=request.args['g']
	return "NO request"+ "gogoanimecode sent is "+gc
@app.route('/anime/<string:name>',methods=['POST'])
def findallepisode():
	pass
