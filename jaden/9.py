#!/usr/bin/env python

import math

minions = int(input())
cockpit_r = float(input())
body_r, body_h = map(float, input().split())
storage_l, storage_w, storage_h = map(float, input().split())

remaining_c = round(4/3 * math.pi * cockpit_r ** 3 - 2.2 - 4.1, 2)
remaining_b = round(body_h * math.pi * body_r ** 2 - 12.1, 2)
remaining_s = round(2 * 1/3 * storage_l * storage_w * storage_h, 2)
minions_need = round(minions * 1.2, 2)

print("Cockpit {:.2f}".format(remaining_c))
print("Body {:.2f}".format(remaining_b))
print("Pods {:.2f}".format(remaining_s))
print("Minions Need {:.2f}".format(minions_need))

if remaining_c + remaining_b + remaining_s >= minions_need:
	print("PLAN ACCEPTED")
else:
	print("PLAN REJECTED")
