import pymysql
import os

import os
host = os.environ['LOCAL_HOST']
user = os.environ['LOCAL_USER']
password = os.environ['LOCAL_PASSWORD']

def create_connection():
    try:
        connection = pymysql.connect(host=host,
                                     user=user,
                                     passwd=password,
                                     db="superstore")
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

def run_stmt(cursor, sql_stmt):
    is_success = True
    try:
        cursor.execute(sql_stmt)
    except pymysql.Error as error:
        print "execute error: ", error
        is_success = False
    return is_success

def run_prepared_stmt(cursor, stmt, paramtrs):
    is_success = True
    try:
        cursor.execute(stmt, paramtrs)
    except pymysql.Error as error:
        print "execute error: ", error
        is_success = False
    return is_success

def destroy_connection(connection):
    connection.close()
