import psycopg2
"""

=== calm-thicket-8451 Config Vars
DATABASE_URL: postgres://
oivlwelvilidjf
DSbFeB1X3knNMeQw-7hpXnbUHG
ec2-54-243-125-2.compute-1.amazonaws.com
5432
d7tqum8ti79ms

HEROKU_POSTGRESQL_ORANGE_URL: postgres://oivlwelvilidjf:DSbFeB1X3knNMeQw-7hpXnbU
HG@ec2-54-243-125-2.compute-1.amazonaws.com:5432/d7tqum8ti79ms

The basic connection parameters are:

dbname – the database name (only in the dsn string)
database – the database name (only as keyword argument)
user – user name used to authenticate
password – password used to authenticate
host – database host address (defaults to UNIX socket if not provided)
port – connection port number (defaults to 5432 if not provided)
"""
conn = psycopg2.connect(database="d7tqum8ti79ms",
                        user="oivlwelvilidjf",
                        password="DSbFeB1X3knNMeQw-7hpXnbUHG",
                        host="ec2-54-243-125-2.compute-1.amazonaws.com"
                        )
cur = conn.cursor()
cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)",
...      (100, "abc'def")
