#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 16:04:00 2020

@author: hex
"""

f = open("data/day13.txt")
depart = int(f.readline())
buses = [int(elem) for elem in f.readline().split(',') if not elem == 'x']
f.close()
curr = depart
while all([curr % bus for bus in buses]):
    curr += 1
print((curr - depart) * [bus for bus in buses if curr % bus == 0][0])
#%%
#I did this part mostly on paper so here's some explanation
#buses are made of [a,d] where a and d are the start and step of an arithmetic sequence
#combine folds left and finds the sequence of times where those buses immediately follow eachother
#xs are just buses that come every minute
#by folding left back to 0 you find the sequence of times where the buses all sequentially follow eachother
#the starting term of this is the t in the problem
def combine(bus1, bus2):
    n2 = 0
    while (bus2[1] * n2 + bus2[0] - bus1[0] - 1) % bus1[1]:
        n2 += 1
    n1 = (bus2[1] * n2 + bus2[0] - bus1[0] - 1) / bus1[1]
    return [[bus1[1] * n1 + bus1[0],bus1[1] * bus2[1]]]
buses = [[0,int(elem)] if not elem == 'x' else [0,1] for elem in open("data/day13.txt").readlines()[1].split(',')]
for i in range(len(buses) - 1, 0, -1):
    bus2 = buses[i]
    bus1 = buses[i - 1]
    remaining = buses[:i - 1]
    buses = remaining + combine(bus1, bus2)
print(int(buses[0][0]))
