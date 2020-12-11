#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 14:09:19 2020

@author: hex
"""

def count_occ(mat, i, j):
    count = 0
    for i_s in range(-1, 2):
        for j_s in range(-1, 2):
            if (i_s or j_s) and i_s + i >= 0 and i_s + i < len(mat) and j_s + j >= 0 and j_s + j < len(mat[0]):
                if mat[i + i_s][j + j_s] == '#':
                    count += 1
    return count
data = [list(x[:-1]) for x in open("Data/day11.txt",'r').readlines()]
changed = True
while changed:
    changed = False
    new = [line.copy() for line in data]
    for i,row in enumerate(data):
        for j,c in enumerate(row):
            if c == 'L' and not count_occ(data, i, j):
                new[i][j] = '#'
                changed = True
            elif c == '#' and count_occ(data, i, j) >= 4:
                new[i][j] = 'L'
                changed = True
    data = [line.copy() for line in new]
print(sum([len([elem for elem in line if elem == '#']) for line in data]))
#%%
def count_occ(mat, i, j):
    count = 0
    for i_d in range(-1, 2):
        for j_d in range(-1, 2):
            if (i_d or j_d):
                i_s = i + i_d
                j_s = j + j_d
                while i_s >= 0 and i_s < len(mat) and j_s >= 0 and j_s < len(mat[0]):
                    if mat[i_s][j_s] == '#':
                        count += 1
                        break
                    elif mat[i_s][j_s] == 'L':
                        break
                    i_s += i_d
                    j_s += j_d
    return count
data = [list(x[:-1]) for x in open("Data/day11.txt",'r').readlines()]
changed = True
while changed:
    changed = False
    new = [line.copy() for line in data]
    for i,row in enumerate(data):
        for j,c in enumerate(row):
            if c == 'L' and not count_occ(data, i, j):
                new[i][j] = '#'
                changed = True
            elif c == '#' and count_occ(data, i, j) >= 5:
                new[i][j] = 'L'
                changed = True
    data = [line.copy() for line in new]
print(sum([len([elem for elem in line if elem == '#']) for line in data]))