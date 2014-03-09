#!/usr/bin/python
from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine
from os import path

def db_connect(db_name, host):
	'''Returns a sqlalchemy database engine based on db_name on host. It uses a my.cnf file in this folder to supply user info.'''
	myDB = URL(drivername='mysql', host='localhost', database=db_name, query={ 'read_default_file' : path.abspath('my.cnf') })
	engine = create_engine(name_or_url=myDB)
	engine.connect() #to test the db connection
	return engine

