from peewee import *
from os import path

def db_connect():
	database_name = 'emailquotes'

	if path.exists('my.cnf'):
        	cnf = path.abspath('my.cnf')
	else:
	        print("Create a mysql config file in this directory.")
	        return

	db = MySQLDatabase(database_name, read_default_file=cnf)
	db.connect() #tests database connection
	return db

