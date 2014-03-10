#!/usr/bin/python
from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine
from os import path

def db_connect(db_name, host):
	cnf_path = path.abspath(path.join(path.dirname(__file__), 'my.cnf'))
	'''Returns a sqlalchemy database engine based on db_name on host. It uses a my.cnf file in this folder to supply user info.'''
	myDB = URL(drivername='mysql', host='localhost', database=db_name, query={ 'read_default_file' : cnf_path })
	engine = create_engine(name_or_url=myDB, echo=False)
	engine.connect() #to test the db connection
	return engine

