#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary:
        new = list(a_dictionary.keys())
        marks = 0
        top = ""
        for i in new:
            if a_dictionary[i] > marks:
                marks = a_dictionary[i]
                top = i
        return top
