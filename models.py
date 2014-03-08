#!/usr/bin/python
from peewee import *
from db_connect import db_connect


db = db_connect()

class User(Model):
	name = CharField()
	email_addresses = TextField()

	class Meta:
		database = db

class Person(Model):
	name = CharField()

	class Meta:
		database = db

class Quote(Model):
	message = TextField()
	send_to = ForeignKeyField(User, related_name='quotes_sent')
	said_by = ForeignKeyField(Person, related_name='quotes_said')
	
	class Meta:
		database = db

