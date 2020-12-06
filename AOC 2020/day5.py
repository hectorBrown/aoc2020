#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 20:24:14 2020

@author: hex
"""

dat = [x[:-1] for x in open("Data/day5.txt",'r').readlines()][:-1]
ids = []
for seat in dat:
    row_ran = 128
    lowest_row = 0
    col_ran = 8
    lowest_col = 0
    for c in seat[:-3]:
        if c == 'B':
            lowest_row += row_ran / 2
        row_ran /= 2
    for c in seat[-3:]:
        if c == 'R':
            lowest_col += col_ran / 2
        col_ran /= 2
    ids.append(lowest_row * 8 + lowest_col)
print(max(ids))
#%%
dat = [x[:-1] for x in open("Data/day5.txt",'r').readlines()][:-1]
ids = []
for seat in dat:
    row_ran = 128
    lowest_row = 0
    col_ran = 8
    lowest_col = 0
    for c in seat[:-3]:
        if c == 'B':
            lowest_row += row_ran / 2
        row_ran /= 2
    for c in seat[-3:]:
        if c == 'R':
            lowest_col += col_ran / 2
        col_ran /= 2
    ids.append(lowest_row * 8 + lowest_col)
ids.sort()
for i, idn in enumerate(ids):
    if ids[i + 1] != idn + 1:
        print(idn + 1)
        break
