#!/usr/bin/python
from models import *
from db_connect import db_connect
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
import smtplib
from email.mime.text import MIMEText

engine = db_connect('emailquotes', 'localhost')
Session = sessionmaker(bind=engine)
session = Session()
message_template = "This is your daily dose of quote, courtesy of the McMaier Expedition:\n\n"
sending_address = "mcmaier-quotes@mcmaier-expedition.com"

for user in session.query(User).all():
	#pick random quote from ones assigned to user
	rand_quote = session.query(Quote).filter(Quote.send_user == user).order_by(func.rand()).first()
	
	#retrive to address from quote
	to_address = rand_quote.send_user.addresses[-1].email_address #selects most recent address
	
	#construct message body
	msg_body = message_template + rand_quote.message

	msg = MIMEText(msg_body)
	msg['Subject'] = 'Your daily dose of quote'
	msg['From'] = sending_address
	msg['To'] = to_address

	smtp_server = smtplib.SMTP('localhost')
	smtp_server.sendmail(sending_address, [to_address], msg.as_string())
	smtp_server.quit()
