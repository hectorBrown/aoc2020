#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 17:36:06 2020

@author: hex
"""
def run(command, pos, _dir):
    if command[0] == 'N':
        pos[1] += command[1]
    elif command[0] == 'E':
        pos[0] += command[1]
    elif command[0] == 'W':
        pos[0] -= command[1]
    elif command[0] == 'S':
        pos[1] -= command[1]
    elif command[0] == 'L':
        _dir = rotate_dir(int(command[1]/90), _dir)
    elif command[0] == 'R':
        _dir = rotate_dir(int((360- command[1])/90), _dir)
    else:
        pos[0] += command[1] * _dir[0]
        pos[1] += command[1] * _dir[1]
    return [pos, _dir]
def rotate_dir(step, _dir):
    for i in range(step):
        if _dir[0] == 1:
            _dir = [0,1]
        elif _dir[1] == 1:
            _dir = [-1,0]
        elif _dir[0] == -1:
            _dir = [0,-1]
        else:
            _dir = [1,0]
    return _dir
data = [[x[:-1][0], int(x[:-1][1:])] for x in open("Data/day12.txt",'r').readlines()]
pos = [0,0]
_dir = [1,0]
for command in data:
    pos, _dir = run(command, pos, _dir)
print(abs(pos[0]) + abs(pos[1]))
#%%
def run(command, pos, way):
    if command[0] == 'N':
        way[1] += command[1]
    elif command[0] == 'E':
        way[0] += command[1]
    elif command[0] == 'W':
        way[0] -= command[1]
    elif command[0] == 'S':
        way[1] -= command[1]
    elif command[0] == 'L':
        way = rotate_way(int(command[1]/90), way)
    elif command[0] == 'R':
        way = rotate_way(int((360- command[1])/90), way)
    else:
        for i in range(command[1]):
            pos[0] += way[0]
            pos[1] += way[1]
    return [pos, way]
def rotate_way(step, way):
    for i in range(step):
        way[0],way[1] = -way[1],way[0]
    return way
data = [[x[:-1][0], int(x[:-1][1:])] for x in open("Data/day12.txt",'r').readlines()]
pos = [0,0]
way = [10,1]
for command in data:
    pos, way = run(command, pos, way)
print(abs(pos[0]) + abs(pos[1]))