import pymysql
import csv
from db_connect import *

def import_product_category():
    is_success = True
    try:
        connection = create_connection()
        # cursor = connection.cursor()
        csvfile = open("SuperstoreSubset.csv", "rb")
        reader = csv.reader(csvfile)
        # list placeholder
        product_categories = []
        for i, row in enumerate(reader):
            # if it's the first row, we ignore it because we don't want to insert headers
            if(i == 0): continue
            # getting product_category data
            product_category = row[9]
            # appending to the list
            product_categories.append(product_category)
        # removing duplicates
        product_categories_nodups = list(set(product_categories))
        # now we must insert the data into a list
        insert_prefix = "INSERT INTO Product_Category(product_category_name) VALUES ('{product_category_name}');"
        for item in product_categories_nodups:
            sql_command = insert_prefix.format(product_category_name= item)
            insert_status = run_insert(sql_command)
            if insert_status is False:
                is_success = False
        commit_status = do_commit(connection)
        if commit_status is False:
            is_success = False
    except IOError as e:
        print "IO Error: " + e.strerror
    return is_success

def destroy_connection(conn):
	conn.close()
# import_product_category()
