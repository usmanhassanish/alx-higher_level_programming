#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = []
    summation = 0
    for num in my_list:
        if num not in new:
            summation += num
            new.append(num)
    return summation
