#!/usr/bin/python3
def multiple_returns(sentence):
    a = ()
    if len(sentence) == 0:
        a = 0, "None"
    else:
        a = len(sentence), sentence[0]
    return a
