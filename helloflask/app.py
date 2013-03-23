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
    return 'Hello Heroku! Here is some DB: {}'.format(record)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)