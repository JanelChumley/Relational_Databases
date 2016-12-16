import pymysql
from db_connect import *
def rollback():
    try:
        delete_stmt = "DELETE FROM Products"
        alter_stmt = "ALTER TABLE Products AUTO_INCREMENT = 1"
        run_delete(delete_stmt)
        run_alter(alter_stmt)
    except IOError as e:
        print "IO Error: " + e.strerror
rollback()