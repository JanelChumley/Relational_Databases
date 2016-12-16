import pymysql
from rollback_order_products import *
from rollback_customer_orders import *
from rollback_products import *
from rollback_product_subcategory import *
from rollback_product_category import *
from rollback_customer import *
from rollback_customer_segment import *



from import_customer_segment import *
from import_customer import *
from import_product_category import *
from import_product_subcategory import *
from import_products import *
from import_customer_orders import *
from import_order_products import *

is_success = import_product_category()
if(is_success):
    print "import_product_category: successful"
else:
    print "import_product_category: failed"

is_success = import_product_subcategory()
if(is_success):
    print "import_product_subcategory: successful"
else:
    print "import_product_subcategory: failed"

is_success = import_products()
if(is_success):
    print "import_products: successful"
else:
    print "import_products: failed"

is_success= import_customer_segment()
if(is_success):
    print "import_customer_segment: successful"
else:
    print "import_customer_segment: failed"

is_success = import_customer()
if(is_success):
    print "import_customer: successful"
else:
    print "import_customer: failed"

is_success = import_customer_orders()
if(is_success):
    print "import_customer_orders: successful"
else:
    print "import_customer_orders: failed"

is_success = import_order_products()
if(is_success):
    print "import_order_products: successful"
else:
    print "import_order_products: failed"

