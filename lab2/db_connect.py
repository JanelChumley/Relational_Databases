import pymysql

def create_connection():
	try:
		connection = pymysql.connect(host="127.0.0.1",   # MySQL hostname
                                     user="root",        # MySQL username, default is root
                                     passwd="jr43872",   # MySQL password
                                     db="superstore")        # MySQL db name
		return connection
	except pymysql.Error as error:
		print "connection error: ", error

def run_insert(insert_stmt):
	try:
		conn = create_connection()
		cursor = conn.cursor()
		cursor.execute(insert_stmt)
		conn.commit()
		destroy_connection(conn)
	except pymysql.Error as error:
		print "insert error: ", error
def run_select(cursor, select_stmt):
    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute(select_stmt)
        # return result
    except pymysql.Error as error:
        print "insert error: ", error
def run_delete(delete_stmt):
	try:
		conn = create_connection()
		cursor = conn.cursor()
		cursor.execute(delete_stmt)
		conn.commit()
	except pymysql.Error as error:
		print "delete error: ", error
def run_alter(alter_stmt):
	try:
		conn = create_connection()
		cursor = conn.cursor()
		cursor.execute(alter_stmt)
		conn.commit()
	except pymysql.Error as error:
		print "alter error: ", error

def do_commit(connection):
	is_success = True
	try:
		connection.commit()
	except pymysql.Error as error:
		print "commit error: ", error
		is_success = False
	return is_success


def destroy_connection(connection):
	connection.close()

