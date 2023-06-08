#!/usr/bin/python3
import sys
argLength = len(sys.argv)

if __name__ == "__main__":
    if argLength > 2:
        print("{} arguments:".format(argLength - 1))
        for x in range(argLength - 1):
            print("{}: {}".format(x + 1, sys.argv[x + 1]))
    elif argLength == 2:
        n = 1
        print("{} argument.".format(argLength-1))
        print("{}: {}".format(n, sys.argv[1]))
    else:
        print("{} arguments.".format(argLength-1))
