#! /usr/bin/python

import json
from OpenSSL import SSL
from flask import Flask, request, make_response, send_from_directory
#from VLAN.main import VLAN



context = SSL.Context(SSL.SSLv23_METHOD)
context.use_privatekey_file('key.pem')
context.use_certificate('cert.pem')

rest_server = Flask(__name__)

logger = open('log','w')

VLANApp = VLAN()


@rest_server.errorhandler(500)
def genError(error):
#raise error
	return make_response("<html><body><center><font color=red><b>ERROR</b></font>" + error.message + "<br/><br/><input type="button" value="Back" onclick="window.history.back();">", 500)

@rest_server.errorhandler(404)
def not_found(error):
	return make_response(json.dumps({'error':Not found'}), 404)

@rest_server.route('/',methods=['GET'])
def main():
	text = open('index.html')
	site = ''
	for line in text:
		site = site + line
	return make_response(site, 200)

@rest_server.route('/vlan',methods=['GET'])
def vlan():
	return make_response(VLANApp.index(), 200)

@rest_server.route('/vlan',methods=['POST'])
def deploy():
	return make_response(VLANApp.main(request.data), 200)

#rest_server.run(host='127.0.01', port=80)
rest_server.run(host='127.0.0.1', port=443, ssl_context=context)
#openssl req -x509 -newkey rsa:5096 -keyout key.pem -out cert.pem -days 365
