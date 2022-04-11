#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 10:57:36 2020

@author: hex
"""
def get_next(history):
    temp = history.copy()
    temp.reverse()
    if temp[0] in temp[1:]:
        return temp[1:].index(temp[0]) + 1
    else:
        return 0
dat = [int(x) for x in open("data/day15.txt",'r').readline()[:-1].split(',')]
target = 2020
for i in range(target - len(dat)):
    dat.append(get_next(dat))
print(dat[-1])
#%%
dat = [int(x) for x in open("data/day15.txt",'r').readline()[:-1].split(',')]
target = 30000000
spoken = {}
for i,term in enumerate(dat[:-1]):
    spoken[term] = i
last = dat[-1]
for i in range(len(dat) - 1, target - 1):
    curr = 0
    if not last in spoken:
        curr = 0
    else:
        curr = i - spoken[last]
    spoken[last] = i
    last = curr
print(last)
