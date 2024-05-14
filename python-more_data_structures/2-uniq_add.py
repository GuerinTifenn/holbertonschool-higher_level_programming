#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_values = set()
    sum_unique = 0
    for i in my_list:
        if i not in unique_values:
            unique_values.add(i)
            sum_unique += i
    return sum_unique
