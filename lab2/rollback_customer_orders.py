import pymysql
from db_connect import *

def rollback():
    try:
        delete_stmt = "DELETE FROM Customer_Orders"
        run_delete(delete_stmt)
    except IOError as e:
		print "IO Error: " + e.strerror
rollback()