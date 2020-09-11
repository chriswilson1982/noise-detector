#!/usr/bin/env python

import httplib
import urllib
import datetime


class PushoverSender:
	def __init__(self, user_key, api_key):
		self.user_key = user_key
		self.api_key = api_key

	def send_notification(self, text):

		now = datetime.datetime.now()
		timestamp = "\n{:02}:{:02} on {:02}/{:02}/{:04}".format(
			now.hour, now.minute, now.day, now.month, now.year)
		text += timestamp

		conn = httplib.HTTPSConnection("api.pushover.net:443")
		post_data = {'user': self.user_key, 'token': self.api_key, 'message': text}
		conn.request("POST", "/1/messages.json", urllib.urlencode(post_data), {"Content-type": "application/x-www-form-urlencoded"})

		print("Push notification triggered at {:02}:{:02} on {:02}/{:02}/{:04}".format(now.hour, now.minute, now.day, now.month, now.year))
		print(conn.getresponse().read())

