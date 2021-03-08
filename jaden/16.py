#!/usr/bin/env python

base_to_mul = {
	"B": 1,
	"KB": 1000,
	"MB": 1000000,
	"GB": 1000000000,
	"TB": 1000000000000,
	"PB": 1000000000000000,
	"EB": 1000000000000000000,
	"ZB": 1000000000000000000000
}

bases = []

amount, base = input().split()
no_bytes = float(amount) * base_to_mul[base]

result = ""

for new_base in ["KiB", "MiB", "GiB", "TiB", "PiB", "EiB", "ZiB"]:
	if no_bytes / 1024 < 1:
		break

	no_bytes /= 1024
	result = "{:.2f} {}".format(round(no_bytes, 2), new_base)

if result == "":
	print("{:.2f} B".format(round(no_bytes, 2)))
else:
	print(result)
