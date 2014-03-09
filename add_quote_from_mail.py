#!/usr/bin/python
from peewee import *
from db_connect import db_connect
from models import Person, User, Quote
import re, email, optparse, sys

'''Takes an email and generates database info for it as a quote.'''

parser = optparse.OptionParser()
parser.add_option("-f", "--file", dest="filename", type="string", 
		help="specify file to import quote from")
parser.add_option("-s", "--stdin", action="store_false", dest="use_file", default=True, help="use stdin for message import instead")

(options, args) = parser.parse_args()

db = db_connect()

if options.use_file:
	try:
		mail_file = open(options.filename)
	except IOError:
		sys.stdout.write("There was an error reading the specified file. Aborting.")
		return
else:
	mail_file = sys.stdin
	if mail_file = '':
		sys.stdout.write("Either us -f to specify a file, or input a message with stdin.")
		return

msg = email.message_from_file(mail_file)

try:
