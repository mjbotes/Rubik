import sys
from functools import wraps
from mix import *

def runXtimes(c):
    x = 1
    if c == '\'':
        x = 3
    elif c.isdigit():
        x = int(c, 10)
    return x

def parser(cube):
    if (sys.argv[1]):
        args = sys.argv[1]
        arr = args.split(" ")
        for rule in arr:
            x = 1
            i = 0
            if (len(rule) > 1):
                x = runXtimes(rule[1])
            if rule[0] == 'L':
                while i < x:
                    moveL(cube)
                    i+=1
            elif rule[0] == 'R':
                while i < x:
                    moveR(cube)
                    i+=1
            elif rule[0] == 'U':
                while i < x:
                    moveU(cube)
                    i+=1
            elif rule[0] == 'D':
                while i < x:
                    moveD(cube)
                    i+=1
            elif rule[0] == 'F':
                while i < x:
                    moveF(cube)
                    i+=1
            elif rule[0] == 'B':
                while i < x:
                    moveB(cube)
                    i+=1