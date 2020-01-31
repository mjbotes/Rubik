from parser import parser

def numR(i):
    if i == 2:
        return "2"
    elif i == 3:
        return "'"

def whiteCross(cube):
    while cube['F'][0][1] != 'F' or cube['F'][1][0] != 'F' or cube['F'][1][2] != 'F' or cube['F'][2][1] != 'F':
        if cube['F'][1][0] == cube['F'][1][2]:
            parser("F R U R' U' F'", cube)
        elif cube['F'][0][1] == cube['F'][2][1]:
            parser("U F R U R' U' F'", cube)
            break
        elif cube['F'][0][1] != 'F' and cube['F'][1][0] != 'F' and cube['F'][1][2] != 'F' and cube['F'][2][1] != 'F':
            parser("F U R U' R' F' U F R U R' U' F'", cube)
            break
        elif cube['F'][1][2] == cube['F'][2][1] or cube['F'][0][1] == cube['F'][1][0]:
            parser("F R U R' U' F'", cube)
        else:
           parser("U",cube)

def findSide(s1, s2, cube):
    r = isSide(s1, cube['F'][0][1], s2, cube['U'][2][1])
    if (r > 0):
        if r == 1:
            return ['F', 0, 1]
        else:
            return ['T', 2, 1]
    r = isSide(s1, cube['F'][1][0], s2, cube['L'][1][2])
    if r > 0:
        if r == 1:
            return ['F', 1, 0]
        else:
            return ['L', 1, 2]
    r = isSide(s1, cube['F'][1][2], s2, cube['R'][1][0])
    if r > 0:
        if r == 1:
            return ['F', 2, 1]
        else:
            return ['R', 1, 0]
    r = isSide(s1, cube['F'][2][1], s2, cube['U'][0][1])
    if r > 0:
        if r == 1:
            return ['F', 2, 1]
        else:
            return ['U', 0, 1]
    r = isSide(s1, cube['B'][0][1], s2, cube['T'][0][1])
    if r > 0:
        if r == 1:
            return ['B', 0, 1]
        else:
            return ['T', 0, 1]
    r = isSide(s1, cube['B'][1][2], s2, cube['R'][1][2])
    if r > 0:
        if r == 1:
            return ['B', 1, 2]
        else:
            return ['R', 1, 2]
    r = isSide(s1, cube['B'][2][1], s2, cube['U'][2][1])
    if r > 0:
        if r == 1:
            return ['B', 2, 1]
        else:
            return ['U', 2, 1]
    r = isSide(s1, cube['B'][1][0], s2, cube['L'][1][0])
    if r > 0:
        if r == 1:
            return ['B', 1, 0]
        else:
            return ['L', 1, 0]
    r = isSide(s1, cube['R'][0][1], s2, cube['T'][1][2])
    if r > 0:
        if r == 1:
            return ['R', 0, 1]
        else:
            return ['T', 1, 2]
    r = isSide(s1, cube['R'][2][1], s2, cube['U'][1][2])
    if r > 0:
        if r == 1:
            return ['R', 2, 1]
        else:
            return ['U', 1, 2]
    r = isSide(s1, cube['L'][0][1], s2, cube['T'][1][0])
    if r > 0:
        if r == 1:
            return ['B', 0, 1]
        else:
            return ['T', 1, 0]
    r = isSide(s1, cube['L'][2][1], s2, cube['U'][1][0])
    if r > 0:
        if r == 1:
            return ['L', 2, 1]
        else:
            return ['U', 1, 0]

def isSide(s1, c1, s2, c2):
    if (s1 == c1) & (s2 == c2):
        return 1
    elif (s1 == c2) & (s2 == c1):
        return 2
    else:
        return -1
