#!/usr/bin/python3
for letter in range(ord('a'), ord('z')+1):
    if (letter == 101) or (letter == 113):
        continue
    print(chr(letter), end="")