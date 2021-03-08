#!/usr/bin/env python

code = input()
lookup = input()

code = [lookup.index(i) for i in code]
code = "".join("{:b}".format(i - 8).zfill(6) for i in code)
code = [code[i:i+8] for i in range(0, len(code), 8)]
code = [int(i, 2) for i in code]
code = "".join(map(chr, code))

print(code)
