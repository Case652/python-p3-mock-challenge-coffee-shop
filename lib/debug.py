#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Customer
from classes.many_to_many import Order
from classes.many_to_many import Coffee

if __name__ == '__main__':
    print("HELLO! :) let's debug")
c1 = Coffee("Mocha")
c2 = Coffee("Dry")
CU1 = Customer("Bill")
CU2 = Customer("Benny")
O1 = Order(CU1,c1,1.99)
O2 = Order(CU1,c2,2.99)
O3 = Order(CU2,c1,3.99)
O4 = Order(CU2,c1,4.99)
ipdb.set_trace()
