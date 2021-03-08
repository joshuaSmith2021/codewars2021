#!/usr/bin/env python

notes = input()

replacements = {
	"!": " not ",
	"&": " and ",
	"|": " or ",
	"T": "True",
	"F": "False"
}

new_notes = []

for i in notes:
	if i == "(" or i == ")":
		new_notes.append(i)
	else:
		new_notes.append(replacements[i])

if eval("".join(new_notes)):
	steps = {
		"!": "1 N",
		"&": "2 W",
		"|": "3 S",
		"T": "4 E",
		"F": "JUMP"
	}

	print("\n".join(steps[i] for i in notes.replace("(", "").replace(")", "")))
else:
	print("I am disinclined to acquiesce to your request")
