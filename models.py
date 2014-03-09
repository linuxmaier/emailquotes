#!/usr/bin/python
from db_connect import db_connect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship, backref

engine = db_connect('emailquotes', 'localhost')

Base = declarative_base()

class User(Base):
	__tablename__ = 'users'

	id = Column(Integer, primary_key=True)
	name = Column(String(50))

	def __repr__(self):
		return "<User(%s)>" % (self.name)

class Quote(Base):
	__tablename__ = 'quotes'

	id = Column(Integer, primary_key=True)
	message = Column(Text())
	send_id = Column(Integer, ForeignKey('users.id'))
	send_user = relationship("User", backref=backref('quotes', order_by=id))
	
	def __repr__(self):
		return "<Quote(id=%s)>" % self.id

class Address(Base):
	__tablename__ = 'addresses'

	id = Column(Integer, primary_key=True)
	email_address = Column(String(25), nullable=False)
	user_id = Column(Integer, ForeignKey('users.id'))

	user = relationship("User", backref=backref('addresses', order_by=id))

	def __repr__(self):
		return "<Address(%s)>" % self.email_address
