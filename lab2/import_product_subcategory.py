import pymysql
import csv
from db_connect import *

def run_select(select_stmt):
	try:
		conn = create_connection()
		cur = conn.cursor()
		cur.execute(select_stmt)
		cat_id = cur.fetchone()
		destroy_connection(conn)
		return cat_id

	except pymysql.Error as error:
		print "insert error: ", error


def import_product_subcategory():
    is_success = True
    try:
        connection = create_connection()
        cur = connection.cursor()
        csvfile = open("SuperstoreSubset.csv", "rb")
        reader = csv.reader(csvfile)
        # this is the list placeholder
        subcat_data = []
        for i, row in enumerate(reader):
            # ignoring headers
            if(i == 0): continue
            # getting desired attributes
            product_subcategory_name = row[10]
            product_category_name = row[9]
            # creating select query to reference surrogate key
            cat_id_query = "SELECT product_category_id FROM Product_Category pc WHERE pc.product_category_name = '" + product_category_name + "'"
            # referencing surrogate key
            cur.execute(cat_id_query)
            result = cur.fetchone()
            cat_id = result[0]
            #appending tuple of attributes to list
            subcat_data.append((product_subcategory_name, cat_id))
        # getting rid of the some of the duplicates
        subcat_data_nodupes = list(set(subcat_data))
        # now we need to insert the data into the table
        insert_prefix = "INSERT INTO Product_Subcategory (product_subcategory_name, product_category_id) VALUES ('{product_subcategory_name}', {product_category_id} );"
        for i in range(len(subcat_data_nodupes)):
            sql_command = insert_prefix.format(product_subcategory_name = subcat_data_nodupes[i][0], product_category_id = subcat_data_nodupes[i][1])
            insert_status = run_insert(sql_command)
            if insert_status is False:
                is_success = False
        commit_status = do_commit(connection)
        if commit_status is False:
            is_success = False
    except IOError as e:
        print "IO Error: " + e.strerror
    return is_success
# import_product_subcategory()