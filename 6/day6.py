#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 20:36:06 2020

@author: hex
"""


data = ''.join(open("data/day6.txt",'r').readlines()).translate({ord('
'): ord(' ')})[:-1].split("  ")
count = 0
for group in data:
    answered = []
    for person in group.split(' '):
        for question in person:
            if not question in answered:
                answered.append(question)
                count += 1
print(count)
#%%
data = ''.join(open("data/day6.txt",'r').readlines()).translate({ord('
'): ord(' ')})[:-1].split("  ")
count = 0
for group in data:
    answered = []
    for person in group.split(' '):
        answered.append(list(person))
    count += len([x for x in answered[0] if all([x in y for y in answered[1:]])])
print(count)
