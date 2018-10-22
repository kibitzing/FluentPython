#!/usr/bin/envs python3
# -*- coding: utf-8 -*-

#################################
#
#       Inha University
#     DSP Lab Sanghong Kim
#
#
#################################

"""
2018_10_18_Fluent_Python
@Author Sanghong.Kim
술집에서 안주 및 술을 사람 수에 대비 많이 시키면 서비스를 주는 시스템
Class를 거의 처음 다뤄 보기에 애를 많이 썻다. 함수를 Class의 input으로 넣고 내부에서 처리가 가능하지만
머리도 많이 써야 되는거 같다.
이 프로그램을 만들다보니 술이 땡긴다.
"""

# Import Modules
import time
import argparse
from collections import namedtuple

Pos = namedtuple('table', 'name person')

class ListItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def list(self):
        return self.product

    def quan(self):
        return self.quantity

    def total(self):
        return self.price * self.quantity


class Order:
    def __init__(self, table, order, service=None):
        self.table = table
        self.order = list(order)
        self.service = service

    def list(self):
        if not hasattr(self, '__list'):
            self.__list = (item.list() for item in self.order)
        return self.__list

    def quan(self):
        if not hasattr(self, '__quan'):
            self.__quan = (item.quan() for item in self.order)
        return self.__quan

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.order)
        return self.__total

    def add(self):
        recipt = {}
        for i in range(0, len(self.order)):
            recipt[(list(self.list())[i])] = (list(self.quan())[i])
        if self.service is None:
            return recipt
        else:
            if not self.service(self) is None:
                recipt[self.service(self)] += 1
            else:
                return recipt
        return recipt

    def __repr__(self):
        fmt = 'Table : {}, Ordered : {}, Total Price: {:.2f}'
        return fmt.format(self.table.name, self.add() ,self.total())

def soju_service(order):
    return list(order.list())[0] if list(order.quan())[0] / order.table.person  >= 2.5 else None

def beer_service(order):
    return list(order.list())[1] if list(order.quan())[1] / order.table.person  >= 3 else None

def total_service(order):
    if order.total() / order.table.person >= 25000:
        return list(order.list())[2]
    elif order.total() / order.table.person >=10000:
        return list(order.list())[3]
    else:
        return None

def time_cal(program):
    # Started Time
    st=time.time()
    # Running Program
    print(program)
    # Ended Time
    et=time.time()
    # Running Time
    return et-st

def main(args):
    print("Add Your Code Below")

    table1 = Pos('table 1', 4)
    order1 = [ListItem('soju', 9 ,3500),
             ListItem('beer', 0, 4000),
             ListItem('soup', 1, 23000),
             ListItem('snack', 1, 5000)
             ]

    table2 = Pos('table 2', 2)
    order2 = [ListItem('soju', 8, 3500),
              ListItem('beer', 0, 4000),
              ListItem('soup', 1, 23000),
              ListItem('snack', 0, 5000)
              ]

    table3 = Pos('table 3', 3)
    order3 = [ListItem('soju', 0, 3500),
              ListItem('beer', 9, 4000),
              ListItem('soup', 0, 23000),
              ListItem('snack', 2, 8000)
              ]

    print("-----------------------------------------------  Snack Service  ------------------------------------------------")
    print("Soju Service  : ",Order(table1, order1, soju_service))
    print("Beer Service  : ",Order(table1, order1, beer_service))
    print("Total Service : ",Order(table1, order1, total_service))

    print("--------------------------------------------- Soup or Soju Service  --------------------------------------------")
    print("Soju Service  : ",Order(table2, order2, soju_service))
    print("Beer Service  : ",Order(table2, order2, beer_service))
    print("Total Service : ",Order(table2, order2, total_service))

    print("--------------------------------------------  Snack or Beer Service  -------------------------------------------")
    print("Soju Service  : ",Order(table3, order3, soju_service))
    print("Beer Service  : ",Order(table3, order3, beer_service))
    print("Total Service : ",Order(table3, order3, total_service))
    print("----------------------------------------------------------------------------------------------------------------")

# Arguments Setting
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    main(args)
