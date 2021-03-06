# coding: UTF-8
import urllib2
import json
import time

# connpassからデータ読み込み
connpass_url = "http://connpass.com/api/v1/event/?count=1000"

time.sleep(1) # 読み込み失敗防止のため、Wait処理を掛ける
resp = urllib2.urlopen(connpass_url).read()
# 読み込んだJSONデータをディクショナリ型に変換
resp = json.loads(resp)

for event in resp["events"]:
	if (event['waiting'] > 0):
		print event['title']
		print "    Limit : " + str(event['limit'])
		print "    Accepted : " + str(event['accepted'])
		print "    Waited : " + str(event['waiting'])
		print "    Date: " + event['started_at']
		print "    URL: " + "http://connpass.com/event/" + str(event['event_id'])
		print "\n\n"
