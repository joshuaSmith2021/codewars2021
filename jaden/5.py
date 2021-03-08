#!/usr/bin/env python

from collections import Counter

doubles = []

with open("input.txt") as file:
	birthdays = [date[:-6] for date in file.readlines()[1:]]
	birthday_f = Counter(birthdays)

	for b in birthdays:
		if b in birthday_f and birthday_f[b] > 1:
			doubles.append(b)
			del birthday_f[b]

print(len(doubles))

if len(doubles) == 0:
	print("duplicates: None")
else:
	print("duplicates: {}".format(" ".join(doubles)))
