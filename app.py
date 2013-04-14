import os
import psycopg2
from flask import Flask

app = Flask(__name__)

CONN = psycopg2.connect(database="d7tqum8ti79ms",
                        user="oivlwelvilidjf",
                        password="DSbFeB1X3knNMeQw-7hpXnbUHG",
                        host="ec2-54-243-125-2.compute-1.amazonaws.com"
                        )
CUR = CONN.cursor()


@app.route('/')
def hello():
    CUR.execute("""SELECT * FROM members LIMIT 5;""")
    record = CUR.next()
    webmap="240fc14f85eb4ca2949074b8ff7dcbbb"
    return """<html>
<head>
<title>Neighborhood Watch Information System</title>
</head>
<body>
<h1>Neighborhood Watch Information System</h1>
<iframe width="500" height="400" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="http://www.arcgis.com/home/webmap/embedViewer.html?webmap={webmap}&amp;extent=-82.4591,28.0088,-82.4389,28.0217"></iframe><br /><small><a href="http://www.arcgis.com/home/webmap/viewer.html?webmap={webmap}&amp;extent=-82.4591,28.0088,-82.4389,28.0217" style="color:#0000FF;text-align:left" target="_blank">View Larger Map</a></small>
</body>
</html>""".format(webmap=webmap)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)