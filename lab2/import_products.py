import pymysql
import csv
from db_connect import *

def import_products():
    is_success = True
    try:
        connection = create_connection()
        cur = connection.cursor()
        csvfile = open("SuperstoreSubset.csv", "rb")
        reader = csv.reader(csvfile)
        # creating list placeholder
        product_data = []
        for i, row in enumerate(reader):
            # ignoring headers
            if(i == 0): continue
            # getting desired attributes
            product_subcategory_name = row[10]
            # escaping single quotes
            product_name = row[12].replace("'", "\\'")
            unit_price = row[3]
            # this is a select query for the surrogate key
            product_subcategory_id_query = "SELECT product_subcategory_id FROM product_subcategory pc WHERE pc.product_subcategory_name = '" + product_subcategory_name + "'"
            #referencing surrgoate key
            cur.execute(product_subcategory_id_query)
            result = cur.fetchone()
            product_subcategory_id= result[0]
            # appending tuple of attributes to list
            product_data.append((product_name,unit_price,product_subcategory_id))
        # eliminating some of the duplicates
        product_data_nodups = list(set(product_data))
        # now we need to insert the data into the table
        insert_prefix = "INSERT INTO Products(product_name,unit_price,product_subcategory_id) VALUES ('{product_name}',{unit_price},'{product_subcategory_id}');"
        for i in range(len(product_data_nodups)):
            sql_command = insert_prefix.format(product_name = product_data_nodups[i][0],unit_price = product_data_nodups[i][1], product_subcategory_id = product_data_nodups[i][2])
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
# import_products()