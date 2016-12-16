import pymysql
import csv
from datetime import datetime
from db_connect import *

def import_customer_orders():
    is_success = True
    try:
        connection = create_connection()
        csvfile = open("SuperstoreSubset.csv", "rb")
        reader = csv.reader(csvfile)
        order_data = []
        #getting the attributes from each row
        for row in reader:
            order_id = row[23]
            customer_id = row[5]
            date = row[18].split("/")
            # this is so we can avoid incomplete date entries
            if(len(date) == 1): continue
            # converting date from mm/dd/yyyy to YYYY-MM-DD
            else:
                order_date = '{:%Y-%m-%d}'.format(datetime(int("20" + date[2]), int(date[0]), int(date[1])))
            order_priority = row[1]
            order_tup = (order_id, customer_id, order_date, order_priority)
            # appending tuple to list
            order_data.append(order_tup)
        # eliminating some of the duplicates
        order_data_nodups = list(set(order_data))
       # now we need to insert the data into the table
        insert_prefix = "INSERT INTO Customer_Orders(order_id, customer_id, order_date, order_priority) VALUES ({order_id},{customer_id},'{order_date}', '{order_priority}');"
        # iterating through the list of data to do the insert
        for i in range(len(order_data_nodups)):
            sql_command = insert_prefix.format(order_id = order_data_nodups[i][0], customer_id= order_data_nodups[i][1],order_date = order_data_nodups[i][2], order_priority = order_data_nodups[i][3])
            insert_status = run_insert(sql_command)
            if insert_status is False:
                is_success = False
        commit_status = do_commit(connection)
        if commit_status is False:
            is_success = False
    except IOError as e:
        print "IO Error: " + e.strerror
    return is_success
# import_customer_orders()