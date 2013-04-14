import os
import psycopg2
from flask import Flask

app = Flask(__name__)

#CONN = psycopg2.connect(database="d7tqum8ti79ms",
#                        user="oivlwelvilidjf",
#                        password="DSbFeB1X3knNMeQw-7hpXnbUHG",
#                        host="ec2-54-243-125-2.compute-1.amazonaws.com"
#                        )
#CUR = CONN.cursor()

HEADER = """<html>
<head>
<title>Neighborhood Watch Information System</title>
<style>
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

<h1>Neighborhood Watch Information System</h1>
<div id="mybox">

<center>"""

@app.route('/pants')
def pants():
    return HEADER + """<body>Pants!<br/>
    <img src="/pants.jpg"/>
</body>
</html>
    """

@app.route('/capn/dandye')
def capn():
    webmap="7fc0d40adb434b3d8c262672ab572d39"
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
    webmap="240fc14f85eb4ca2949074b8ff7dcbbb"
    html = HEADER
    html +="""
<iframe width="1024" height="768" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="http://www.arcgis.com/home/webmap/embedViewer.html?webmap={webmap}&amp;extent=-82.4591,28.0088,-82.4389,28.0217"></iframe><br /><small><a href="http://www.arcgis.com/home/webmap/viewer.html?webmap={webmap}&amp;extent=-82.4591,28.0088,-82.4389,28.0217" style="color:#0000FF;text-align:left" target="_blank">View Larger Map</a></small>
</center>
</body>
</html>""".format(webmap=webmap)
    return html

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)