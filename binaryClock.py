#!/usr/bin/python
# -*- coding: utf-8 -*-
import time

class Watches(object):
	"""Binary Clock"""
	def __init__(self, hour, minute, second):
		self.time = hour, minute, second
		self.time_bin = self.intToByte(hour), self.intToByte(minute), self.intToByte(second), 
	def intToByte(self, x):
		n = "" if x>0 else "0"
		while x > 0:
			y = str(x % 2)
			n = y + n
			x = int(x / 2)
		return n
	def __repr__(self):
		return "%s : %s : %s \n%s : %s : %s "% (self.time_bin[0], self.time_bin[1], self.time_bin[2], self.time[0], self.time[1], self.time[2])

print Watches(time.localtime()[3], time.localtime()[4], time.localtime()[5])
