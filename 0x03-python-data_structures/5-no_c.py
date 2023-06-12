#!/usr/bin/python3
def no_c(my_string):
    remove_char = "c"
    remove_char2 = "C"
    new_string = ""
    for x in my_string:
        if x != remove_char and x != remove_char2:
            new_string += x
    return new_string

