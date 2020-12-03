# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 11:59:49 2020

@author: Hector
"""

f = open("Data\day3.txt")
dat = f.readlines()
_map = [list(x[:-1]) for x in dat]
pos = [0,0]
counter = 0
while pos[0] < len(_map):
    if _map[pos[0]][pos[1]] == '#':
        counter += 1
    pos[0] += 1
    pos[1] += 3
    if pos[1] >= len(_map[0]):
        pos[1] -= len(_map[0])
print(counter)
#%%

def count(slope):
    pos = [0,0]
    counter = 0
    while pos[0] < len(_map):
        if _map[pos[0]][pos[1]] == '#':
            counter += 1
        pos[0] += slope[1]
        pos[1] += slope[0]
        if pos[1] >= len(_map[0]):
            pos[1] -= len(_map[0])
    return counter
f = open("Data\day3.txt")
dat = f.readlines()
_map = [list(x[:-1]) for x in dat]
slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]
counts = [count(x) for x in slopes]
prod = 1
for c in counts:
    prod *= c
print(prod)