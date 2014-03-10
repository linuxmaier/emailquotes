emailquotes
===========

emailquotes is a program that collects emails sent to it in a database, then when run picks one of those commands to email back to the user who sent it in.

requires sqlalchemy

setup notes
-----------

Make sure to pre-create the database emailquotes (or change the name in the files; maybe someday I'll make that simpler). also make sure there's an emailquotes user that has privileges on that database.

create a my.cnf in the same directory as db\_connect.py, as that's where it will look for the cnf.
