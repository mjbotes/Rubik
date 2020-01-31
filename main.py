import models
from printCube import *
from parser import parser
from solve import whiteCross
import sys

def main():
	cube = models.faces
	parser(sys.argv[1] ,cube)
	whiteCross(cube)
	printCube(cube)

if __name__ == "__main__":
	main()