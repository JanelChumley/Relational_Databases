import pymysql
from db_connect import *
def rollback():
    try:
        delete_stmt = "DELETE FROM Customer_Segment"
        alter_stmt = "ALTER TABLE Customer_Segment AUTO_INCREMENT = 1"
        run_delete(delete_stmt)
        run_alter(alter_stmt)
    except IOError as e:
        print "IO Error: " + e.strerror
rollback()
