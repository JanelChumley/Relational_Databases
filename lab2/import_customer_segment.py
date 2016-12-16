import pymysql
import csv
from db_connect import *

def import_customer_segment():
    is_success = True
    try:
        connection = create_connection()
        csvfile = open("SuperstoreSubset.csv", "rb")
        reader = csv.reader(csvfile)
        # list placeholder
        customer_segments = []
        # if it's the first row, we ignore it because the first row contains headers
        for i, row in enumerate(reader):
            if(i == 0): continue
            # if it isn't the first row, get the customer segment data and append it to the list
            customer_segments.append(row[8])
        # getting rid of duplicates
        customer_segments_nodups = list(set(customer_segments))
        insert_prefix = "INSERT INTO Customer_Segment(customer_segment_name) VALUES ('{customer_segment_name}');"
        # now we need to insert the data into the table
        for i, item in enumerate(customer_segments_nodups):
            sql_command = insert_prefix.format(customer_segment_name = item)
            insert_status = run_insert(sql_command)
            if insert_status is False:
                is_success = False
                return is_success
        commit_status = do_commit(connection)
        if commit_status is False:
            is_success = False
    except IOError as e:
		print "IO Error: " + e.strerror
    return is_success
# import_customer_segment()