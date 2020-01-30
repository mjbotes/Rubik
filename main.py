import models
from printCube import *
from parser import parser

def main():
	cube = models.faces
	parser(cube)
	printCube(cube)

if __name__ == "__main__":
	main()