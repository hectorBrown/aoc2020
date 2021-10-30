#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 09:23:40 2020

@author: hex
"""

data = [x[:-1].split(' ') for x in open("Data/day8.txt").readlines()]
acc = 0
i = 0
visited = []
while True:
    command = data[i]
    visited.append(i)
    if command[0] == "acc":
        acc += int(command[1])
        i += 1
    elif command[0] == "jmp":
        i += int(command[1])
    elif command[0] == "nop":
        i += 1
    if i in visited:
        break
print(acc)
#%%
def valid(commands):
    i = 0
    acc = 0
    visited = []
    while True:
        command = commands[i]
        visited.append(i)
        if command[0] == "acc":
            acc += int(command[1])
            i += 1
        elif command[0] == "jmp":
            i += int(command[1])
        elif command[0] == "nop":
            i += 1
        if i in visited:
            return False
        elif i == len(commands) - 1:
            return True
def getacc(commands):
    i = 0
    acc = 0
    while True:
        command = commands[i]
        if command[0] == "acc":
            acc += int(command[1])
            i += 1
        elif command[0] == "jmp":
            i += int(command[1])
        elif command[0] == "nop":
            i += 1
        if i == len(commands):
            break
    return acc
    
data = [x[:-1].split(' ') for x in open("Data/day8.txt").readlines()]
for i,command in enumerate(data):
    if command[0] == "nop" or command[0] == "jmp":
        new = data.copy()
        new[i] = data[i].copy()
        new[i][0] = "jmp" if command[0] == "nop" else "nop"
        if valid(new):
            print(getacc(new))
    