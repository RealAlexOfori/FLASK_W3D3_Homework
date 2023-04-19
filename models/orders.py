from models.order import *

order1 = Order("Alex", "24 September 2023", 5, "The Bible", 1)
order2 = Order("Peter", "15 May 2023", 7, "The Hitmakers", 2)
order3 = Order("John","16 November 2023", 1, "Think And Grow Rich", 3)
orders = [order1, order2, order3]

def get_order(order_id):
    return orders[order_id-1]