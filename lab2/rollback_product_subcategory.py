import pymysql
from db_connect import *
def rollback():
    try:
        delete_stmt = "DELETE FROM Product_Subcategory"
        alter_stmt = "ALTER TABLE Product_Subcategory AUTO_INCREMENT = 1"
        run_delete(delete_stmt)
        run_alter(alter_stmt)
    except IOError as e:
		print "IO Error: " + e.strerror
rollback()
