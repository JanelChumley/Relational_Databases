import pymysql
from db_connect import *
def rollback():
    try:
        delete_stmt = "DELETE FROM Customer"
        run_delete(delete_stmt)
    except IOError as e:
		print "IO Error: " + e.strerror
# def destroy_connection(conn):
#     conn.close()
rollback()