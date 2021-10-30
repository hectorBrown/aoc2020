#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 19:07:52 2020

@author: hex
"""

data = [int(x[:-1]) for x in open("Data/day10.txt",'r').readlines()]
data.sort()
differences = [min(data), 3]
for i,adap in enumerate(data):
    if i != 0:
        differences.append(adap - data[i - 1])
print(len([x for x in differences if x == 1]) * len([x for x in differences if x == 3]))
#%%
class Adapter:
    def __init__(self, value):
        self.parents = []
        self.val = value
        self.routes = 1
data = [int(x[:-1]) for x in open("Data/day10.txt",'r').readlines()]
data.sort()
adapters = {0: Adapter(0)}
routes = {0: 0}
for value in data:
    adapters[value] = Adapter(value)
    for i in range(value - 3, value):
        if i in adapters:
            adapters[value].parents.append(adapters[i])
    adapters[value].routes = sum([parent.routes for parent in adapters[value].parents])
print(adapters[data[-1]].routes)