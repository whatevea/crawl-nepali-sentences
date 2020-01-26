from flask import Flask,request
app=Flask(__name__)
@app.route('/')
def giveiframe():
	link=request.args['link']
	link=link.replace('^','/')
	tag=f'''<html><head><style></style></head><body style="margin:0;"><iframe style="border: 0; width: 100%; height: 100%" id="embed-responsive-item" src="{link}" marginwidth=0 marginheight=0 scrolling="no" allowfullscreen="true" frameborder="0" scrolling="no"></iframe></body></html>'''
	return tag
