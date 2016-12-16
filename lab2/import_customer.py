import pymysql
import csv
from db_connect import *

def import_customer():
    is_success = True
    try:
        connection = create_connection()
        cur = connection.cursor()
        csvfile = open("SuperstoreSubset.csv", "rb")
        reader = csv.reader(csvfile)
        customer_data = []
        for i, row in enumerate(reader):
            if(i == 0): continue
            customer_segment_name = row[8]
            customer_segment_id_query = "SELECT customer_segment_id FROM Customer_Segment pc WHERE pc.customer_segment_name = '" + customer_segment_name  + "'"
            # getting surrogate key from the customer_segment table
            cur.execute(customer_segment_id_query)
            result = cur.fetchone()
            customer_segment_id= result[0]
            customer_id = row[5]
            # this escapes single quotes
            customer_name = row[6].replace("'", "\\'")
            state = row[15]
            city = row [16]
            postal_code = row[17]
            region = row[14]
            customer_tup = (customer_id, customer_name,city,state, postal_code, region, customer_segment_id)
            # appending customer_tup to customer_data
            customer_data.append(customer_tup)
        # taking list of set of customer_data to eliminate some of the duplicate entries
        customer_data_nodups = list(set(customer_data))
        insert_prefix = "INSERT INTO Customer(customer_id, customer_name,city,state, postal_code, region,customer_segment_id)VALUES ('{customer_id}', '{customer_name}','{city}','{state}','{postal_code}','{region}', '{customer_segment_id}');"
        for i, row in enumerate(customer_data_nodups):
            sql_command = insert_prefix.format(customer_id = customer_data_nodups[i][0], customer_name= customer_data_nodups[i][1],city=customer_data_nodups[i][3],state = customer_data_nodups[i][3], postal_code= customer_data_nodups[i][4], region = customer_data_nodups[i][5],customer_segment_id = customer_data_nodups[i][6])
            run_insert(sql_command)
            if run_insert(sql_command) is False:
                is_success = False
        commit_status = do_commit(connection)
        if commit_status is False:
            is_success = False
    except IOError as e:
		print "IO Error: " + e.strerror
    return is_success

# import_customer()