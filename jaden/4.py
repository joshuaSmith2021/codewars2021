#!/usr/bin/env python

with open("input.txt") as file:
	for line in reversed(file.readlines()[1:]):
		print(line, end="")
