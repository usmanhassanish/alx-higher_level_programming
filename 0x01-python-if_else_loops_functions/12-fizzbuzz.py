#!/usr/bin/python3
def fizzbuzz():
    for j in range(1, 101):
        if ((j % 5 == 0) and (j % 3 == 0)):
            print("fizzbuzz", end=" ")
        elif (j % 3 == 0):
            print("fizz", end=" ")
        elif (j % 5 == 0):
            print("buzz", end=" ")
        else:
            print(j, end=" ")
