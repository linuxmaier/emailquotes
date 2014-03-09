#!/usr/bin/python
from db_connect import db_connect
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from models import *
from email import message_from_file
import re, optparse, sys

parser = optparse.OptionParser()
parser.add_option("-f", "--file", dest="filename", type="string",
		help="specify file to import quote from")
parser.add_option("-s", "--stdin", action="store_false", dest="use_file",
		default=True, help="use stdin for message import")

(options, args) = parser.parse_args()

if options.use_file:
	try:
		mail_file = open(options.filename)
	except IOError:
		sys.stdout.write("There was an error reading the specified file. Aborting.")
		return
else:
	mail_file = sys.stdin
	if mail_file = '':
		sys.stdout.write("Either use -f to specify a file or input a message with stdin.")
		return

msg = message_from_file(mail_file)

email_pattern = re.compile('([a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+[a-zA-Z0-9-])')
name_pattern = re.compile('([A-Za-z]+ [A-Za-z]+)')
quote_from_name = name_pattern.search(msg.get('from')).group(1)
quote_from_address = email_pattern.search(msg.get('from')).group(1)

if msg.is_multipart() is False:
	msg_body = msg.get_payload()
else:
	for payload in msg.get_payload():
		if payload.get_content_subtype() == 'plain':
			msg_body = payload.get_payload()
			break

#remove \r from string because Windows >.<
msg_body = re.sub(r'\\r', '', msg_body)

quotes = msg_body.split('\n\n')

#now actually connect to database
engine = db_connect('emailquotes', 'localhost')
Session = sessionmaker(bind=engine)
session = Session()

#create user if it doesn't already exist
try:
	user_address = session.query(Address).filter(Address.email_address == quote_from_address).one()
	user_name = user_address.user
except NoResultFound:
	try:
		user_name = session.query(User).filter(User.name == quote_from_name).one()
	except NoResultFound:
		user_name = User(name=quote_from_name)
	user_address = Address(email_address=quote_from_address, user=user)



for quote in quotes:
	

