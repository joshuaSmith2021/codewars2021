#!/usr/bin/env python

with open("input.txt") as file:
	code = list(file.readlines())

coords = []

for y in range(len(code)):
	for x in range(len(code[0]) - 3):
		if code[y][x] == "M" and code[y][x + 1] == "O" and code[y][x + 2] == "J" and code[y][x + 3] == "O":
			coords = [(y, x), (y, x + 1), (y, x + 2), (y, x + 3)]
			break

		if code[y][x + 3] == "M" and code[y][x + 2] == "O" and code[y][x + 1] == "J" and code[y][x] == "O":
			coords = [(y, x + 3), (y, x + 2), (y, x + 1), (y, x)]
			break

for y in range(len(code) - 3):
	for x in range(len(code[0])):
		if code[y][x] == "M" and code[y + 1][x] == "O" and code[y + 2][x] == "J" and code[y + 3][x] == "O":
			coords = [(y, x), (y + 1, x), (y + 2, x), (y + 3, x)]
			break

		if code[y + 3][x] == "M" and code[y + 2][x] == "O" and code[y + 1][x] == "J" and code[y][x] == "O":
			coords = [(y + 3, x), (y + 2, x), (y + 1, x), (y, x)]
			break

for y in range(len(code) - 1):
	for x in range(len(code[0]) - 1):
		if code[y][x] == "M" and code[y][x + 1] == "O" and code[y + 1][x] == "J" and code[y + 1][x + 1] == "O":
			coords = [(y, x), (y, x + 1), (y + 1, x), (y + 1, x + 1)]

print("M: {},{}".format(coords[0][1], coords[0][0]))
print("O: {},{}".format(coords[1][1], coords[1][0]))
print("J: {},{}".format(coords[2][1], coords[2][0]))
print("O: {},{}".format(coords[3][1], coords[3][0]))
