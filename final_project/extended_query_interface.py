import pymysql
from db_connect import *

def print_menu():
    print "What would you like to show?"
    print "1. Number of products by category"
    print "2. Customers by region"
    print "3. Customers by segment"
    print "4. Number of orders by region"
    print "5. Number of orders by year"
    print "6. Average unit price by product category"
    print "7. Twitter data related to searches on calculators and keyboards"
    print "8. Exit the program"


def num_products_cat_query():
    is_success = True
    # Here are the queries for each of the options
    #unit price by category

    print "You have chosen to show the number of products by category. What category would you like to choose?"
    print "1. Technology"
    print "2. Office Supplies"
    print "3. Furniture"
    print "4. All product categories"
    choice = input("Enter your choice [1-4]: ")
    if choice in (1,2,3):
        stmt = "SELECT product_category_name, COUNT(*) num_products\n" \
               "FROM product_vw\n" \
               "GROUP BY product_category_name\n" \
               "HAVING product_category_name = %s;"
        if choice == 1:
            paramtrs = 'Technology'
        elif choice == 2:
            paramtrs = 'Office Supplies'
        elif choice == 3:
            paramtrs = 'Furniture'
    elif choice == 4:
        stmt = "SELECT product_category_name, COUNT(*) num_products FROM product_vw GROUP BY product_category_name;"
    else:
        print "Wrong choice! Try again: "
        num_products_cat_query()

    try:
        connection = create_connection()
        cursor = connection.cursor()
        if choice in (1,2,3):
            query_status = run_prepared_stmt(cursor,stmt,(paramtrs))
        # calling run_stmt since the query for all product categories doesn't require parameters
        else:
            query_status = run_stmt(cursor, stmt)
        if query_status is False:
            is_success = False

        results = cursor.fetchall()
        print ""
        for row in results:
            print row
        print ""

    except pymysql.Error as e:
        is_success = False
        print "products by category: " + str(e)

    return is_success
def num_products_cat_query():
    is_success = True
    # Here are the queries for each of the options
    #unit price by category

    print "You have chosen to show the number of products by category. What category would you like to choose?"
    print "1. Technology"
    print "2. Office Supplies"
    print "3. Furniture"
    print "4. All product categories"
    choice = input("Enter your choice [1-4]: ")
    stmt = "SELECT product_category_name, COUNT(*) num_products\n" \
           "FROM product_vw\n" \
           "GROUP BY product_category_name\n" \
           "HAVING product_category_name = %s;"
    if choice in (1,2,3):
        if choice == 1:
            paramtrs = 'Technology'
        elif choice == 2:
            paramtrs = 'Office Supplies'
        elif choice == 3:
            paramtrs = 'Furniture'
    elif choice == 4:
        stmt = "SELECT product_category_name, COUNT(*) num_products FROM product_vw GROUP BY product_category_name;"
    else:
        print "Wrong choice! Try again "
        num_products_cat_query()

    try:
        connection = create_connection()
        cursor = connection.cursor()
        if (choice in (1, 2, 3)):
            query_status = run_prepared_stmt(cursor, stmt, (paramtrs))
        #calling run_stmt since the query for all categories doesn't require parameters
        else:
            query_status = run_stmt(cursor, stmt)
        if query_status is False:
            is_success = False

        results = cursor.fetchall()
        print ""
        for row in results:
            print row
        print ""

    except pymysql.Error as e:
        is_success = False
        print "number of products by category: " + str(e)

    return is_success

def customers_region_query():
    is_success = True
    print "You have chosen to explore customer counts by region. What would you like to choose?"
    print "1. Central"
    print "2. East"
    print "3. West"
    print "4. South"
    print "5. All regions"
    choice = input("Enter your choice [1-5]: ")
    if choice in (1,2,3,4):
        stmt = "SELECT region, COUNT(*) num_orders FROM order_vw WHERE region = %s;"
        if choice == 1:
            paramtrs = 'Central'
        elif choice == 2:
            paramtrs = 'East'
        elif choice == 3:
            paramtrs = 'West'
        elif choice == 4:
            paramtrs = 'South'
    elif choice == 5:
        stmt = "SELECT region, COUNT(*) num_customers FROM customer_vw GROUP BY region;"
    else:
        print "Wrong choice! Try again: "
        customers_region_query()
    while choice in (1, 2, 3, 4,5):
        try:
            connection = create_connection()
            cursor = connection.cursor()
            if (choice in (1, 2, 3,4)):
                query_status = run_prepared_stmt(cursor, stmt, (paramtrs))
            # calling run_stmt since the query for all regions doesn't require parameters
            else:
                query_status = run_stmt(cursor, stmt)
            if query_status is False:
                is_success = False

            results = cursor.fetchall()
            print ""
            for row in results:
                print row
            print ""
        except pymysql.Error as e:
            is_success = False
            print "customers by region query: " + str(e)

        return is_success
def customers_segment_query():
    is_success = True
    print "You have chosen to show the number of customers by customer segment. What segment would you like to choose?"
    print "1. Home Office"
    print "2. Consumer"
    print "3. Corporate"
    print "4. Small Business"
    print "5. All segments"
    choice = input("Enter your choice [1-5]: ")
    if choice in (1,2,3,4):
        stmt = "SELECT cs.customer_segment_name, COUNT(*) num_customers\n" \
               "FROM Customer c INNER JOIN Customer_Segment cs\n" \
               "ON c.customer_segment_id = cs.customer_segment_id\n" \
               "GROUP BY cs.customer_segment_name\n" \
               "HAVING customer_segment_name = %s;"
        if choice == 1:
            paramtrs = 'Home Office'
        elif choice == 2:
            paramtrs = 'Consumer'
        elif choice == 3:
            paramtrs = 'Corporate'
        elif choice == 4:
            paramtrs = 'Small Business'
    elif choice == 5:
        stmt = "SELECT customer_segment_name, COUNT(*) num_customers FROM customer_vw GROUP BY customer_segment_name;"
    else:
        print "Wrong choice! Try again: "
        customers_segment_query()
    while (choice in (1, 2, 3, 4,5)):
        try:
            connection = create_connection()
            cursor = connection.cursor()
            if (choice in (1, 2, 3,4)):
                query_status = run_prepared_stmt(cursor, stmt, (paramtrs))
            # calling run_stmt since the query for all customer segments doesn't require parameters
            else:
                query_status = run_stmt(cursor, stmt)
            if query_status is False:
                is_success = False

            results = cursor.fetchall()
            print ""
            for row in results:
                print row
            print ""
        except pymysql.Error as e:
            is_success = False
            print "customers by region query: " + str(e)

        return is_success
def num_orders_region_query():
    is_success = True

    print "You have chosen to explore order counts by region. What would you like to choose?"
    print "1. Central"
    print "2. East"
    print "3. West"
    print "4. South"
    print "5. All regions"

    choice = input("Enter your choice [1-5]: ")
    if (choice in (1, 2, 3,4)):
        stmt = "SELECT region, COUNT(*) num_orders FROM order_vw GROUP BY region HAVING region = %s;"
        if choice == 1:
            paramtrs ='Central'
        elif choice == 2:
            paramtrs ='East'
        elif choice == 3:
            paramtrs ='West'
        elif choice == 4:
            paramtrs ='South'
    elif choice == 5:
        stmt = "SELECT EXTRACT(YEAR FROM order_date) year, COUNT(*) num_orders FROM order_vw GROUP BY year;"
    else:
        print ("That's not a valid input. Please try again" )
        num_orders_region_query()

    while(choice in (1,2,3,4,5)):
        try:
            connection = create_connection()
            cursor = connection.cursor()
            if (choice in (1, 2, 3,4)):
                query_status = run_prepared_stmt(cursor, stmt, (paramtrs))
            # calling run_stmt since the query for all regions doesn't require parameters
            else:
                query_status = run_stmt(cursor, stmt)
            if query_status is False:
                is_success = False

            results = cursor.fetchall()
            print ""
            for row in results:
                print row
            print ""

        except pymysql.Error as e:
            is_success = False
            print "num_orders by region query: " + str(e)

        return is_success
def num_orders_year_query():
    is_success = True

    print "You have chosen order counts by year. What would you like to choose?"
    print "1. 2010"
    print "2. 2011"
    print "3. 2012"
    print "4. All years: 2010-2012"
    choice = input("Enter your choice [1-4]: ")
    if(choice in (1,2,3)):
        stmt = "SELECT EXTRACT(YEAR FROM order_date) year, COUNT(*) num_orders\n" \
               "FROM order_vw\n" \
               "GROUP BY year\n" \
               "HAVING year = %s;"
        if choice == 1:
            paramtrs = 2010
        elif choice == 2:
            paramtrs = 2011
        elif choice == 3:
            paramtrs = 2012
    elif choice == 4:
        stmt = "SELECT EXTRACT(YEAR FROM order_date) year, COUNT(*) num_orders\n" \
               "FROM order_vw\n" \
               "GROUP BY year;"
    else:
        print "Wrong choice! Try again: "
        num_orders_year_query()
    try:
        connection = create_connection()
        cursor = connection.cursor()
        if (choice in (1, 2, 3)):
            query_status = run_prepared_stmt(cursor, stmt, (paramtrs))
        # calling run_stmt since the query for all years doesn't require parameters
        else:
            query_status = run_stmt(cursor, stmt)
        if query_status is False:
            is_success = False

        results = cursor.fetchall()
        print ""
        for row in results:
            print row
        print ""

    except pymysql.Error as e:
        is_success = False
        print "num_orders by year query: " + str(e)

    return is_success
def ave_unit_price_cat_query():
    is_success = True
    print "You have chosen to show the number of products by category. What category would you like to choose?"
    print "1. Technology"
    print "2. Office Supplies"
    print "3. Furniture"
    print "4. All product categories"
    choice = input("Enter your choice [1-4]: ")
    stmt = "SELECT * FROM product_cat_ave_price_vw WHERE product_category_name = %s;"
    if choice in (1,2,3):
        if choice == 1:
            paramtrs = 'Technology'
        elif choice == 2:
            paramtrs = 'Office Supplies'
        elif choice == 3:
            paramtrs = 'Furniture'
    elif choice == 4:
        stmt = "SELECT * FROM product_cat_ave_price_vw;"
    else:
        print "Wrong choice! Try again: "
        num_products_cat_query()

    try:
        connection = create_connection()
        cursor = connection.cursor()
        if (choice in (1, 2, 3)):
            query_status = run_prepared_stmt(cursor, stmt, (paramtrs))
        # this is for a query that doesn't require parameters
        else:
            query_status = run_stmt(cursor, stmt)
        if query_status is False:
            is_success = False

        results = cursor.fetchall()
        print ""
        for row in results:
            print row
        print ""

    except pymysql.Error as e:
        is_success = False
        print "number of products by category: " + str(e)

    return is_success

def tweets():
    is_success = True
    print "You have chosen to explore twitter data related to calculators and keyboards. What would you like to choose?"
    print "1. Tweets from searches related to product name"
    print "2. Tweet counts by product name"
    print "3. Tweet counts by product subcategory name"
    print "4. Retweets from searches related to product name"
    print "5. Retweet counts by product name"
    print "6. Retweet counts by product subcategory"
    choice = input("Enter your choice [1-6]: ")
    if choice in (1, 2, 3):
        if choice == 1:
            stmt = "select * from tweet_product_view"
        elif choice == 2:
            stmt = "select product_name, count(*)\n" \
                   "FROM tweet_product_view\n" \
                   "group by product_name\n" \
                   "order by count(*) desc;"
        elif choice == 3:
            stmt = "select product_subcategory_name, count(*)\n" \
                   "FROM tweet_product_view\n" \
                   "group by product_subcategory_name\n" \
                   "order by count(*) desc;"
    elif choice in (4, 5, 6):
        if choice == 4:
            stmt = "select * from rt_view"
        elif choice == 5:
            stmt = "select product_name, count(*) from rt_view group by product_name;"
        elif choice == 6:
            stmt = "select product_subcategory_name, count(*) from rt_view group by product_subcategory_name;"
    else:
        print "Wrong choice! Try again: "
        tweets()
    try:
        connection = create_connection()
        cursor = connection.cursor()
        query_status = run_stmt(cursor, stmt)
        if query_status is False:
            is_success = False

        results = cursor.fetchall()
        print ""
        for row in results:
            print row
        print ""


    except pymysql.Error as e:
        is_success = False
        print
        "tweets by product names and by product subcategory: " + str(e)

    return is_success
while True:
    print_menu()
    choice = input("Enter your choice [1-8]: ")
    if choice==1:
        num_products_cat_query()

    elif choice==2:
        customers_region_query()
    elif choice == 3:
        customers_segment_query()
    elif choice == 4:
        num_orders_region_query()
    elif choice ==5:
        num_orders_year_query()
    elif choice == 6:
        ave_unit_price_cat_query()
    elif choice == 7:
        tweets()
    elif choice==8:
        print "Sorry to see you go. Goodbye!"
        break
    else:
        print "Wrong choice! Try again: "
        print_menu()
        choice = input("Enter your choice [1-8]: ")

