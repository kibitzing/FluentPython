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
2018_10_17_Fluent_Python
@Author Sanghong.Kim
Wave Equation을 풀어 point Source에서 나오는 음향의 Propagation을 구하고 이를 mp4형태로 저장하는 프로그램
"""

# Import Modules
import time
import os
import sys
import argparse
from abc import ABC, abstractmethod
from collections import namedtuple
import numpy as np
import math as m
import imageio
from scipy import misc

dx = 0.1
dt = 0.01
sz_x = 1024
sz_y = 1024
steps = 2000

class wave_simulation:

    def __init__(self, dx_in, dt_in, sz_x_in, sz_y_in, steps_in, broadcast_func_in):
        self.dx = dx_in
        self.dt = dt_in
        self.sz_x = sz_x_in
        self.sz_y = sz_y_in
        self.steps = steps_in
        self.broadcast_func = broadcast_func_in

    def Laplace(self, u_array, dx):
        sz_x = u_array.shape[0]
        sz_y = u_array.shape[1]

        dx2 = np.zeros((sz_x,sz_y), float)
        dy2 = np.zeros((sz_x, sz_y), float)


        dx2[1:sz_x - 1, 1:sz_y - 1] = ((u_array[0:(sz_x - 2), 1:(sz_y - 1)] - u_array[1:(sz_x - 1),
                                                                              1:(sz_y - 1)]) / dx - (
                                               u_array[1:(sz_x - 1), 1:(sz_y - 1)] - u_array[2:sz_x,
                                                                                     1:(sz_y - 1)]) / dx) / dx
        dy2[1:sz_x - 1, 1:sz_y - 1] = ((u_array[1:(sz_x - 1), 0:(sz_y - 2)] - u_array[1:(sz_x - 1),
                                                                              1:(sz_y - 1)]) / dx - (
                                               u_array[1:(sz_x - 1), 1:(sz_y - 1)] - u_array[1:(sz_x - 1),
                                                                                     2:sz_y]) / dx) / dx

        return (dx2 + dy2)

    def Edge_detect(self, c_array):
        dx = np.zeros((sz_x,sz_y), float)
        contour = np.zeros((sz_x,sz_y),float)
        dx[0:(sz_x - 1), 0:(sz_y - 1)] = (
                    np.abs(c_array[0:(sz_x - 1), 1:(sz_y)] - c_array[1:(sz_x), 1:(sz_y)]) + np.abs(
                c_array[1:(sz_x), 0:(sz_y - 1)] - c_array[1:(sz_x), 1:(sz_y)]) > 0)
        contour[dx>0]=1

        return (contour)

    def run(self):
        u_array = np.zeros((self.sz_x, self.sz_y),float)
        u_array_v = np.zeros((self.sz_x, self.sz_y), float)

        arr_new_r = np.zeros((self.sz_x, self.sz_y), float)
        arr_new_g = np.zeros((self.sz_x, self.sz_y), float)
        arr_new_b = np.zeros((self.sz_x, self.sz_y), float)

        outputdata = np.zeros((self.sz_x, self.sz_y, 3), int)

        writer = imageio.get_writer('./output.mp4', fps=30)

        for t in range(0, self.steps):
            b_el, b_el_mask, c = self.broadcast_func(t)

            u_array[b_el_mask == 1] = b_el[b_el_mask == 1]
            u_array_v = u_array_v + np.multiply(np.square(c), self.Laplace(u_array, self.dx) * self.dt)
            u_array = u_array + u_array_v * self.dt

            arr_new = u_array
            arr_new[b_el_mask == 1] = 0

            arr_new_r = np.maximum(arr_new, 0) / np.max(np.maximum(arr_new, 0) + 1e-100)
            arr_new_g = np.minimum(arr_new, 0) / np.min(np.minimum(arr_new, 0) + 1e-100)
            arr_new_b[b_el_mask == 1] = 1

            arr_new_b[self.Edge_detect(c) == 1] = 1
            outputdata[0:self.sz_x, 0:self.sz_y, 0] = arr_new_r[0:self.sz_x, 0:self.sz_y] * 255
            outputdata[0:self.sz_x, 0:self.sz_y, 1] = arr_new_g[0:self.sz_x, 0:self.sz_y] * 255
            outputdata[0:self.sz_x, 0:self.sz_y, 2] = arr_new_b * 255

            print(t,"/",self.steps)
            writer.append_data(outputdata)

def point(t):
    broadcast_el = np.zeros((sz_x, sz_y), float)
    broadcast_el_mask = np.zeros((sz_x, sz_y), int)

    broadcast_el[0, 0:sz_x] = 0
    broadcast_el_mask[0, 0:sz_y] = 1
    broadcast_el[512, 512] = m.sin(2 * m.pi * t * 0.02)
    broadcast_el_mask[512, 512] = 1

    c_const = 6
    c = np.ones((sz_x, sz_y), float) * c_const
    c[0:1, 0:1] = c_const * 0.5

    return broadcast_el, broadcast_el_mask, c

def time_cal(program):
    # Started Time
    st=time.time()
    # Running Program
    print(program)
    # Ended Time
    et=time.time()
    # Running Time
    return et-st

Customer = namedtuple('Customer', 'name fidelity')




class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price* self.quantity


class Order:
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due:{:.2f}>'
        return fmt.format(self.total(),self.due())


class Promotion(ABC):

    @abstractmethod
    def discount(self, order):
        """할인액을 구체적인 숫자로 반환"""

class FidelityPromo(Promotion):
    """1000 이상 -> 5% 할인 적용"""

    def discount(self, order):
        return order.total() * .05 if order.customer.fidelity >= 1000 else 0

class BulkItemPromo(Promotion):
    """20개 이상의 동일 상품 구입 -> 10% 할인 적용"""
    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * .1
            return discount

class LargeOrderPromo(Promotion):
    """10종류 이상의 상품 구입 -> 전체 7% 할인"""
    def discount(self, order):
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * .07
        return 0


def main(args):
    print("Add Your Code Below")

    joe = Customer('John Doe', 0)
    ann = Customer('Ann Smith', 1100)
    cart = [LineItem('banana', 4, .5), LineItem('apple', 10, 1.5), LineItem('watermellon', 5, 5.0)]
    banana_cart = [LineItem('banana', 30, .5), LineItem('apple', 10, 1.5)]
    long_order = [LineItem(str(item_code),1,1.0)
                  for item_code in range(10)]

    print(Order(joe, cart ,FidelityPromo()))
    print(Order(ann, cart, FidelityPromo()))
    print(Order(joe, banana_cart, BulkItemPromo()))
    print(Order(joe, long_order, LargeOrderPromo()))
    print(Order(joe, cart, LargeOrderPromo()))

    sim = wave_simulation(dx, dt, sz_x, sz_y, steps, point)
    sim.run()


# Arguments Setting
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    print("실행시 output.mp4 파일이 생성됩니다.")
    reply = str(input("동의 하십니까? [y/n] ")).lower().strip()
    if reply[:1] == 'y':
        main(args)
    elif reply[:1] == 'n':
        print("코드가 길어서 죄송합니다.")
    else:
        sys.exit()
