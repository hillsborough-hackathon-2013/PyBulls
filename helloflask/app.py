import os
import psycopg2
from flask import Flask
from jinja2 import Environment

# My Modules
import secrets

app = Flask(__name__)

# Globals 
SECRETS = secrets.Secrets()
HTML = """
<html>
<head>
<title>Neighborhood Watch Information System</title>
</head>
<body>
<h1>Neighborhood Watch Information System</h1>
<iframe width="500" height="400" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="http://www.arcgis.com/home/webmap/embedViewer.html?webmap={{webmap}}&amp;extent=-82.4591,28.0088,-82.4389,28.0217"></iframe><br /><small><a href="http://www.arcgis.com/home/webmap/viewer.html?webmap={{webmap}}&amp;extent=-82.4591,28.0088,-82.4389,28.0217" style="color:#0000FF;text-align:left" target="_blank">View Larger Map</a></small>
 
 
</body>
</html>
"""

CONN = psycopg2.connect(SECRETS.database,
                        SECRETS.user,
                        SECRETS.password,
                        SECRETS.host
                        )
CUR = CONN.cursor()

# Functions


@app.route('/<role>/<uname>/')
def view():
    webmap="7fc0d40adb434b3d8c262672ab572d"
    #return 'Hello Heroku! Here is some DB: {}'.format(record)   
    return Environment().from_string(HTML).render(webmap=webmap)


@app.route('/')
def hello():
    CUR.execute("""SELECT * FROM members LIMIT 5;""")
    record = CUR.next()
    webmap="240fc14f85eb4ca2949074b8ff7dcbbb"
    #return 'Hello Heroku! Here is some DB: {}'.format(record)   
    return Environment().from_string(HTML).render(webmap=webmap)

# Context    

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)