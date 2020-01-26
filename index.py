# https://crawl-nepali-sentences-git-iframewithoutsandbox.sandipbamrel.now.sh/
from flask import Flask,jsonify,request
import requests
import re
from bs4 import BeautifulSoup as bs
app=Flask(__name__)
app.config['DEBUG']=True
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
  q=request.args['q']
  print(q)
  url='https://vidstreaming.io/'+q
  html=requests.get(url).text
  soup=bs(html,'html.parser')
  php="https:"+soup.iframe['src']
  phppage=requests.get(php).text
  regex = r"'https://redirecto[^']+'"
  matches = re.search(regex, phppage)
  if matches:
    start=matches.start()
    end=matches.end()
    videourl=phppage[start:end]
    print(videourl)
    notstripped=tag=f'''
  <body>
    <video
      id="my-video"
      class="video-js"
      controls
      preload="auto"
      width="640"
      height="264"
      poster="videoposter.jpg"
      data-setup="">
      <source src={videourl} type="video/mp4" />
    </video>
 '''
  else:
  	try:
  		soup=bs(phppage,'html.parser')
  		xtream=soup.find('li',text='Xstreamcdn')['data-video'].replace('/','^')
  		videourl='https://crawl-nepali-sentences-git-iframewithoutsandbox.sandipbamrel.now.sh/?link='+xtream
  		notstripped=f'<iframe id="embed-responsive-item" src="{videourl}" marginwidth=0 marginheight=0 scrolling="no" width="640" height="500" allowfullscreen="true" frameborder="0" scrolling="no" sandbox="allow-scripts allow-same-origin"></iframe>'
  	except:
  		iframe=html.find('<iframe')
  		iframe2=html.find('>',iframe)+1
  		notstripped=html[iframe:iframe2]
  		if notstripped=="":
  			notstripped="<h2>Episode not valid or is not yet available</h2>"
  response=jsonify({"if":notstripped})
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

