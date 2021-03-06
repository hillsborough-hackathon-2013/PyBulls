import os
from flask import Flask

app = Flask(__name__)

HEADER = """<html>
<head>
<title>Community Geographic Information System</title>
<style>
   @import url("http://fonts.googleapis.com/css?family=Open+Sans:400italic,400");
   @import url("http://fonts.googleapis.com/css?family=Raleway:400,900,700,800,600,500,300,200,100");
   @import url("http://fonts.googleapis.com/css?family=Libre+Baskerville:400,700,400italic");
   @import url("http://fonts.googleapis.com/css?family=Open+Sans:300italic,400italic,600italic,700italic,800italic,300,400,300,600,700,800");
   body{
        font-family: 'Verdana';
    }
    .dash{
        background-color: rgb(255, 255, 255);
        color: rgb(255, 255, 255);
        cursor: auto;
        display: inline-block;
        font-family: Raleway, 'Open Sans', Segoe, 'Helvetica Neue', Helvetica, Arial, sans-serif;
        font-size: 23px;
        font-weight: 800;
        height: 1px;
        letter-spacing: 3px;
        line-height: 27px;
        text-align: center;
        text-transform: uppercase;
        transition-delay: 0s, 0s;
        transition-duration: 0.3s, 0.3s;
        transition-property: color, background-color;
        transition-timing-function: ease-out, ease-out;
        vertical-align: middle;
        width: 70px;
    }    
    .w0{
        color: rgb(216, 205, 222);
        cursor: auto;
        display: inline;
        font-family: Raleway, 'Open Sans', Segoe, 'Helvetica Neue', Helvetica, Arial, sans-serif;
        font-size: 23px;
        font-weight: 300;
        height: auto;
        letter-spacing: 3px;
        line-height: 27px;
        text-align: center;
        text-transform: uppercase;
        transition-delay: 0s, 0s;
        transition-duration: 0.3s, 0.3s;
        transition-property: color, background-color;
        transition-timing-function: ease-out, ease-out;
        width: auto;
    }
    
    #hackhillslogo{
        color: rgb(216, 205, 222);
        background: rgba(2,43,66,0.7);
        font-size: 22.5px;
        line-height: 27px;
        letter-spacing: 3px;
        padding: 0 0 10px;
        font-family: Raleway, 'Open Sans', Segoe, 'Helvetica Neue', Helvetica, Arial, sans-serif;
        font-size: 23px;
        font-weight: 800;
        height: auto;
        letter-spacing: 3px;
        line-height: 27px;
        text-align: center;
        text-transform: uppercase;
        transition-delay: 0s, 0s;
        transition-duration: 0.3s, 0.3s;
        transition-property: color, background-color;
        transition-timing-function: ease-out, ease-out;
        width: auto;
        }
    #mybox{
        border: 10px solid black;
        border-radius:15px;
        display: inline-block;
    };
</style>
</head>
<body>
<center>

<h1 id="hackhillslogo">
<b>
  <span class="dash"></span><span class="w0"> 2013 </span><span class="dash"></span> <br>
  <span class="w3">Hillsborough</span>
  <span class="w3">Hackathon</span>
</b>
</h1>

<h1>Community Geographic Information System</h1>
<div id="mybox">

<center>"""

@app.route('/pants')
def pants():
    return HEADER + """<body>Pants!<br/>
    <img src="/static/pants.jpg"/>
</body>
</html>
    """

@app.route('/capn/dandye')
def capn():
    webmap="7cd8e154a0d547adb65ca9633054a181"
    html = HEADER
    html +="""
    Block Captain's View<br>
<iframe width="1024" height="768" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="http://www.arcgis.com/home/webmap/embedViewer.html?webmap={webmap}&amp;extent=-82.4591,28.0088,-82.4389,28.0217"></iframe><br /><small><a href="http://www.arcgis.com/home/webmap/viewer.html?webmap={webmap}&amp;extent=-82.4591,28.0088,-82.4389,28.0217" style="color:#0000FF;text-align:left" target="_blank">View Larger Map</a></small>
</center>
</body>
</html>""".format(webmap=webmap)
    return html

@app.route('/capn/carolyakimo')
def capn():
    webmap="302079082f7e43d59195c198169491f8"
    html = HEADER
    html +="""
    Block Captain's View<br>
<iframe width="1024" height="768" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="http://www.arcgis.com/home/webmap/embedViewer.html?webmap={webmap}&amp;extent=-82.4591,28.0088,-82.4389,28.0217"></iframe><br /><small><a href="http://www.arcgis.com/home/webmap/viewer.html?webmap={webmap}&amp;extent=-82.4591,28.0088,-82.4389,28.0217" style="color:#0000FF;text-align:left" target="_blank">View Larger Map</a></small>
</center>
</body>
</html>""".format(webmap=webmap)
    return html

@app.route('/capn/susanelbare')
def capn():
    webmap="0a72046352e44ad78ac65c204921bbdd"
    html = HEADER
    html +="""
    Block Captain's View<br>
<iframe width="1024" height="768" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="http://www.arcgis.com/home/webmap/embedViewer.html?webmap={webmap}&amp;extent=-82.4591,28.0088,-82.4389,28.0217"></iframe><br /><small><a href="http://www.arcgis.com/home/webmap/viewer.html?webmap={webmap}&amp;extent=-82.4591,28.0088,-82.4389,28.0217" style="color:#0000FF;text-align:left" target="_blank">View Larger Map</a></small>
</center>
</body>
</html>""".format(webmap=webmap)
    return html

@app.route('/')
def hello():
    #CUR.execute("""SELECT * FROM members LIMIT 5;""")
    #record = CUR.next()
    webmap="5cfe6cefb7e74869940c1fba8ded34aa"
    html = HEADER
    html +="""
    Public View<br>
<iframe width="1024" height="768" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="http://www.arcgis.com/home/webmap/embedViewer.html?webmap={webmap}&amp;extent=-82.4591,28.0088,-82.4389,28.0217"></iframe><br /><small><a href="http://www.arcgis.com/home/webmap/viewer.html?webmap={webmap}&amp;extent=-82.4591,28.0088,-82.4389,28.0217" style="color:#0000FF;text-align:left" target="_blank">View Larger Map</a></small>
</center>
</body>
</html>""".format(webmap=webmap)
    return html

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
