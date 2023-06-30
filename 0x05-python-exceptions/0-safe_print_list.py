#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    len = 0
    for length in my_list:
        len = len + 1
    try:
        if x <= 0:
            raise Exception
    except Exception:
        print("An exception occurred!")
    else:
        if x > len:
            for index in range(len):
                if index == len - 1:
                    print(my_list[index])
                    break
                print(my_list[index], end='')
            return len
        else:
            for index in range(x):
                if index == x - 1:
                    print(my_list[index])
                    break
                print(my_list[index], end='')
            return x
