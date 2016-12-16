import pymysql
import csv
from db_connect import *

def import_order_products():
    is_success = True
    try:
        connection = create_connection()
        cursor = connection.cursor()
        csvfile = open("SuperstoreSubset.csv", "rb")
        reader = csv.reader(csvfile)
        order_items_data = []
        for i, row in enumerate(reader):
            if(i == 0): continue
            # this escapes any single quotes
            product_name = row[12].replace("'", "\\'")
            product_id_query = "SELECT product_id FROM Products pc WHERE pc.product_name = '" + product_name + "'"
            # this is for the surrogate key from the product_id table
            cursor.execute(product_id_query)
            result = cursor.fetchone()
            product_id = result[0]
            # getting the remaining attributes
            order_id = row[23]
            order_quantity = row[21]
            #creating a tuple of the attributes
            order_tup = (order_id, product_id, product_name, order_quantity)
            # appending the tuple to the list
            order_items_data.append(order_tup)
        # elminating some of the duplicates
        order_data_nodups = list(set(order_items_data))
        # now we need to insert the data into the table
        insert_prefix = "INSERT INTO Order_Products(order_id, product_id,product_name,order_quantity) VALUES ({order_id},{product_id},'{product_name}', {order_quantity});"
        for i in range(len(order_data_nodups)):
            sql_command = insert_prefix.format(order_id = order_data_nodups[i][0], product_id = order_data_nodups[i][1],product_name = order_data_nodups[i][2], order_quantity= order_data_nodups[i][3])
            insert_status = run_insert(sql_command)
            if insert_status is False:
                is_success = False
        commit_status = do_commit(connection)
        if commit_status is False:
            is_success = False
    except pymysql.Error as e:
        print "import_order_products error: " + e.strerror
    return is_success
# import_order_products()