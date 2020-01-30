
def printFace(A):
    n = 3
    for i in range(n): 
        print(A[i]) 

def printCube(C):
    print("FRONT")
    print("=====")
    printFace(C['F'])
    print("UNDER")
    print("=====")
    printFace(C['U'])
    print("BACK")
    print("=====")
    printFace(C['B'])
    print("TOP")
    print("=====")
    printFace(C['T'])
    print("RIGHT")
    print("=====")
    printFace(C['R'])
    print("LEFT")
    print("=====")
    printFace(C['L'])
