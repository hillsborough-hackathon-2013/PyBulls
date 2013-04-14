#!/usr/bin/env python3.3

import feedparser
from urllib.parse import urlparse, parse_qs
import json
import sys
import psycopg2

feed = feedparser.parse("http://www.tampagov.net/appl_rss_feeds/rss.asp?feed=police_calls")
try:
  con = psycopg2.connect(database="pybulls_gis", user='ckim', password="")
except:
  print("can't connect")

cur = con.cursor();

#CONN = psycopg2.connect(database="d7tqum8ti79ms",
#                        user="oivlwelvilidjf",
#                        password="DSbFeB1X3knNMeQw-7hpXnbUHG",
#                        host="ec2-54-243-125-2.compute-1.amazonaws.com"


feed_data = []
for entry in feed.entries:
  uri = urlparse(entry.link)
  params = parse_qs(uri.query)
  x = params['X'][0]
  y = params['Y'][0]
  cur.execute("insert into police_calls(link, title, pubdate, description, guid, x, y, geom) select %s, %s, %s, %s, %s, "+x+","+y+",ST_Transform(ST_GeomFromText('POINT("+x+" "+y+")', 9105), 4326)",
   [entry.link, entry.title, entry.published, entry.description, entry.id])
con.commit()

#   feed_data.append({
#     'title': entry.title,
#     'link': entry.link,
#     'pubDate' : entry.published,
#     'desc': entry.summary_detail.value,
#     'guid': entry.id,
#     'x': x,
#     'y': y
#     })
# print(json.dumps(feed_data))
