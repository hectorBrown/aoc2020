#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 11:16:32 2020

@author: hex
"""
def valid(rules,prop):
    validity = []
    for rule in rules:
        rulevaliditiy = any([prop >= ran[0] and prop <= ran[1] for ran in rules[rule]])
        validity.append(rulevaliditiy)
    if not any(validity):
        return False
    else:
        return True
data = ''.join(open("Data/day16.txt",'r')).split("\n\n")
rules = {x.split(':')[0]:[[int(z) for z in y.split('-')] for y in x.split(':')[1].split(" or ")] for x in data[0].split("\n")}
my_tick = [int(x) for x in data[1].split('\n')[1].split(',')]
near_ticks = [[int(y) for y in x.split(',')] for x in data[2].split('\n')[1:-1]]
error_rate = 0
for near_tick in near_ticks:
    for prop in near_tick:
        if not valid(rules, prop):
            error_rate += prop
print(error_rate)
#%%
def valid(rules,prop):
    validity = []
    for rule in rules:
        rulevalidity = any([prop >= ran[0] and prop <= ran[1] for ran in rules[rule]])
        validity.append(rulevalidity)
    return any(validity)
def valid_rules(rules,prop):
    valid_rules = []
    for rule in rules:
        rulevalidity = any([prop >= ran[0] and prop <= ran[1] for ran in rules[rule]])
        if rulevalidity:
            valid_rules.append(rule)
    return valid_rules
data = ''.join(open("Data/day16.txt",'r')).split("\n\n")
rules = {x.split(':')[0]:[[int(z) for z in y.split('-')] for y in x.split(':')[1].split(" or ")] for x in data[0].split("\n")}
my_tick = [int(x) for x in data[1].split('\n')[1].split(',')]
near_ticks = [[int(y) for y in x.split(',')] for x in data[2].split('\n')[1:-1]]
to_pop = []
for i, near_tick in enumerate(near_ticks):
    for prop in near_tick:
        if not valid(rules, prop):
            to_pop.append(i)
near_ticks = [tick for i,tick in enumerate(near_ticks) if i not in to_pop]
prop_ind = {}
ind_list = {}
loop = True
while loop:
    for tick in near_ticks:
        for i,prop in enumerate(tick):
            v_r = valid_rules(rules,prop)
            if not i in ind_list:
                ind_list[i] = v_r
            drop = []
            for a,prop2 in enumerate(ind_list[i]):
                if prop2 not in v_r or (prop2 in [ind_list[key][0] for key in ind_list if len(ind_list[key]) == 1] and len(ind_list[i]) > 1):
                    drop.append(a)
            ind_list[i] = [x for i,x in enumerate(ind_list[i]) if not i in drop]
    loop = not all([len(ind_list[ind]) == 1 for ind in ind_list])
prop_ind = {ind_list[key][0]:key for key in ind_list}
dept_ind = [prop_ind[key] for key in prop_ind if key.split(' ')[0] == "departure"]
prod = 1
for ind in dept_ind:
    prod *= my_tick[ind]
print(prod)