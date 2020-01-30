#!/usr/bin/env python3

import mathFC
import models
from printCube import *

def moveU(cube):
	temp = [cube['F'][0][0], cube['F'][0][1], cube['F'][0][2]]
	i = 0
	while i < 3:
		cube['F'][0][i] = cube['R'][0][i]
		i +=1
	i = 0
	while i < 3:
		cube['R'][0][i] = cube['B'][0][i]
		i +=1
	i = 0
	while i < 3:
		cube['B'][0][i] = cube['L'][0][i]
		i +=1
	i = 0
	while i < 3:
		cube['L'][0][i] = temp[i]
		i +=1
	mathFC.rotate90Clockwise(cube['U'])

def moveL(cube):
	temp = [cube['F'][2][0], cube['F'][1][0], cube['F'][0][0]]
	i = 0
	while i < 3:
		cube['F'][i][0] = cube['T'][i][0]
		i +=1
	i = 0
	while i < 3:
		cube['T'][i][0] = cube['B'][i][0]
		i +=1
	i = 0
	while i < 3:
		cube['B'][i][0] = cube['U'][i][0]
		i +=1
	i = 0
	while i < 3:
		cube['U'][i][0] = temp[i]
		i +=1
	mathFC.rotate90Clockwise(cube['L'])

def moveR(cube):
	temp = [cube['F'][2][2], cube['F'][1][2], cube['F'][0][2]]
	i = 0
	while i < 3:
		cube['F'][i][2] = cube['U'][i][2]
		i +=1
	i = 0
	while i < 3:
		cube['U'][i][2] = cube['B'][i][2]
		i +=1
	i = 0
	while i < 3:
		cube['B'][i][2] = cube['T'][i][2]
		i +=1
	i = 0
	while i < 3:
		cube['T'][i][2] = temp[i]
		i +=1
	mathFC.rotate90Clockwise(cube['R'])

def moveF(cube):
	temp = [cube['T'][2][0], cube['T'][2][1], cube['T'][2][2]]
	i = 0
	while i < 3:
		cube['T'][2][i] = cube['L'][i][2]
		i +=1
	i = 0
	while i < 3:
		cube['L'][i][2] = cube['U'][0][i]
		i +=1
	i = 0
	while i < 3:
		cube['U'][0][i] = cube['R'][i][0]
		i +=1
	i = 0
	while i < 3:
		cube['R'][i][0] = temp[i]
		i +=1
	mathFC.rotate90Clockwise(cube['F'])

def main():
	cube = models.faces
	#moveU(cube)
	printCube(cube)
	print("Move Right")
	#moveR(cube)
	printCube(cube)
	print("Move Left")
	#moveL(cube)
	printCube(cube)
	print("Move Left")
	moveF(cube)
	printCube(cube)
if __name__ == "__main__":
	main()