#!/usr/bin/env python

time_start, time_rescue = input().split()

hours, minutes, seconds = map(int, time_start.split(":"))
seconds_start = hours * 60 * 60 + minutes * 60 + seconds
hours, minutes, seconds = map(int, time_rescue.split(":"))
seconds_rescue = hours * 60 * 60 + minutes * 60 + seconds
delta_t = seconds_rescue - seconds_start + 40

delta_cm = 500 - 1 * delta_t

if delta_cm < 0:
	delta_cm = 0

print("{:.2f}".format(round(delta_cm / 100, 2)))

dots = int(delta_cm / 20)

for _ in range(5):
	print("|" + " " * dots + "|")

print("|" + "." * dots + "|")

if delta_cm < 20:
	print("CURSE MY METAL BODY, I WASN'T FAST ENOUGH!")
elif delta_cm == 20:
	print("THIS IS SOME RESCUE!")
else:
	print("THE FORCE WAS WITH YOU")
