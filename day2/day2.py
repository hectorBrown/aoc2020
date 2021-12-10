#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 10:05:57 2020

@author: Hector
"""


def valid(l):
    char = l[0][-1:]
    passw = l[1][1:]
    _range = [int(x) for x in l[0][:-1].split('-')]
    return passw.count(char) >= _range[0] and passw.count(char) <= _range[1]

f = open("data/day2.txt")
dat = [x[:-1].split(':') for x in f.readlines()]
print(len(list(filter(valid, dat))))
#%%
def valid(l):
    char = l[0][-1:]
    passw = l[1][1:]
    _range = [int(x) for x in l[0][:-1].split('-')]
    num = ''.join([passw[_range[0] - 1], passw[_range[1] - 1]]).count(char)
    return num == 1

f = open("data/day2.txt")
dat = [x[:-1].split(':') for x in f.readlines()]
print(len(list(filter(valid, dat))))
