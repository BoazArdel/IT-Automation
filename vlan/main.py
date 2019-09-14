#! /usr/bin/python

import json
import urllib

import add_vlan


class VLAN:
	def __init__(self):
		self.logger = open('vlanlog', 'w')

	def index(self):
		try:
			text = open('VLAN/index.html')
			site = ''
			for line in text:
				site += line
			return site
		except Exception, e:
			self.logger.write(str(e.message))
			raise e
		

		tmp = []
		for entry in fields:
			tmp.append(entry.split('=', 1)[1])
		self.vars = tmp
		
		return self.add()

	def add(self):
		result = add_vlan.deploy(self.vars[2].replace('+', ' '),self.vars[3],urllib.unqoute(self.vars[4]),self.vars[1],self.vars[0])
		return "<html><body><center><font color=red><b>ERROR</b></font>" + result + "<br/><br/><input type="button" value="Back" onclick="window.history.back();">"
