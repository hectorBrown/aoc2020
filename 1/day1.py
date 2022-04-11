#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 13:14:47 2020

@author: Hector
"""

f = open("data/day1.txt",'r')
dat = [int(x[:-1]) for x in f.readlines()]
for i,x in enumerate(dat[:-1]):
    for y in dat[i + 1:]:
        if x + y == 2020:
            print(x*y)

#%%
f = open("data/day1.txt",'r')
dat = [int(x[:-1]) for x in f.readlines()]
for i,x in enumerate(dat):
    others = dat.copy()
    others.pop(i)
    for j,y in enumerate(others):
        others_2 = others.copy()
        others_2.pop(j)
        for k,z in enumerate(others_2):
            if x + y + z == 2020:
                print(x*y*z)
