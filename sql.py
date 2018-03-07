# !/usr/bin/env python
#coding=utf-8
import MySQLdb

conn = MySQLdb.connect(
    host='172.29.XXX.XXX',
    port=3306,
    user='root',
    passwd='XXXXXXX',
    db='athena',
    charset='utf8')
cur = conn.cursor()
cur.execute("delete from user_device")
cur.close()
conn.commit()
conn.close()
