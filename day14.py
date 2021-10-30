#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 12:01:19 2020

@author: hex
"""
def assign(add, mask, mem, val):
    val = list(val)
    for i,c in enumerate(mask):
        if c != 'X':
            val[i] = c
    mem[add] = decimal(''.join(val))
def binary(val):
    res = ""
    for i in range(35, -1, -1):
        if val >= 2**i:
            res += "1"
            val -= 2**i
        else:
            res += "0"
    return res
def decimal(val):
    val = list(val)
    val.reverse()
    val = ''.join(val)
    res = 0
    for i,c in enumerate(val):
        if c == '1':
            res += 2**i
    return res
data = [x[:-1].split(" = ") for x in open("Data/day14.txt",'r').readlines()]
mask = ""
mem = {}
for command in data:
    if  command[0] == "mask":
        mask = command[1]
    else:
        assign(int(command[0][4:-1]),mask,mem,binary(int(command[1])))
print(sum([mem[key] for key in mem]))
#%%
def assign(add, mask, mem, val):
    add = list(add)
    for i,c in enumerate(mask):
        if c == '1':
            add[i] = '1'
        elif c == 'X':
            add[i] = 'X'
    add = ''.join(add)
    add = explode(add)
    for loc in add:
        mem[decimal(loc)] = val
def explode(add):
    res = []
    if 'X' in add:
        for child in explode(add[add.index('X') + 1:]):
            res.append(add[:add.index('X')] + "0" + child)
            res.append(add[:add.index('X')] + "1" + child)
    else:
        return [add]
    return res
def binary(val):
    res = ""
    for i in range(35, -1, -1):
        if val >= 2**i:
            res += "1"
            val -= 2**i
        else:
            res += "0"
    return res
def decimal(val):
    val = list(val)
    val.reverse()
    val = ''.join(val)
    res = 0
    for i,c in enumerate(val):
        if c == '1':
            res += 2**i
    return res
data = [x[:-1].split(" = ") for x in open("Data/day14.txt",'r').readlines()]
mask = ""
mem = {}
for command in data:
    if  command[0] == "mask":
        mask = command[1]
    else:
        assign(binary(int(command[0][4:-1])),mask,mem,int(command[1]))
print(sum([mem[key] for key in mem]))