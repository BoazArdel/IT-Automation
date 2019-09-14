#!/usr/bin/python

import sys
import pexpect
import getopt
import psycopg2

def run(user,passwd, command):
	p = pexpect.spawn("ssh " + user + "@127.0.0.1 -p 8022")
	p.sendline('yes\n')
	p.expect('Password:')
	p.sendline(passwd)
	if p.expect(['NA>','Password:']) == 0:
		p.sendline(command)
		p.expect('NA>')
		result = p.before
		p.sendline('exit')
		return result
	else:
		p.kill(1)
		return "Could not connect to NA, User or Password incorrect"


def deploy(group, user, vlanid, vlanname):
	cred = open("/home/boaz/VLAN/DB_Cred.lck", 'r')
	db = psycopg2.connect(host = '127.0.0.1', database = 'na', port = 5432, user=cred.readline().srtip('\n'), password=cred.readline().srtip('\n'))
	cursor = db.cursor()
	cursor.execute("select d.DeviceID from RN_DEVICE as d, RN_DEVICE_GROUP as dg, RN_DEVICE_GROUP_MAP as g2d where dg.DeviceGroupName='" + group + "' and d.DeviceID=g2d.DeviceID and dg.DeviceID=g2d.DeviceGroupID")
	#preperred statment

	result = cursor.fatchall()
	
	status = ''
	for row in results:
		command = "add vlan -deviceid " + str(row[0]) + " -vlanid " + vlanid + " -vlanname \"" + vlanname + "\""
		status = status + run(user, password, command) 
	
	#select d.primaryipaddress from nas.RN_DEVICE as d, nas.RN_DEVICE_GROUP as dg, nas.RN_DEVICE_MAP as g2d where dg.DeviceGroupName='bla' and d.DeviceID=g2d.DeviceID and dg.DeviceGroupID=g2d.DeviceGroupID

	db.close()
	return status