#!/usr/bin/env python

buildings = []

for _ in range(int(input())):
	height, address = input().split()

	buildings.append((int(height), address))

buildings.sort()

matrix = []

for h, a in buildings:
	matrix.append("*" * h + "~")


maxlen = max(map(len, matrix))

for i in reversed(range(maxlen)):
	for j in range(len(buildings)):
		if len(matrix[j]) - 1 < i:
			print(" ", end="")
		else:
			print(matrix[j][i], end="")

	print()

for _, a in buildings:
	print(a, end="")

print()
