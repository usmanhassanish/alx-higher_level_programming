#!/usr/bin/python3
def pow(a, b):
    result = 1
    if b > 0:
        for i in range(1, b + 1):
            result *= a
    elif b == 0:
        result = 1
    else:
        num = -1 * b
        for k in range(1, num + 1):
            result *= a
        result = 1/result
    return result
