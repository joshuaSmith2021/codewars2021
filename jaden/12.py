#!/usr/bin/env python

contraption, speed, unit_distance, _, unit_time = input().split()

distance_conv = {
	"MILES": 5280 / 3.28,
	"YARDS": 3 / 3.28,
	"FEET": 1 / 3.28,
	"INCHES": 1 / 12 / 3.28,
	"KILOMETERS": 1000,
	"METERS": 1,
	"CENTIMETERS": 1 / 100
}

time_conv = {
	"HOUR": 1 / 60 / 60,
	"MINUTE": 1 / 60,
	"SECOND": 1
}

speed = float(speed)
speed = speed * distance_conv[unit_distance] * time_conv[unit_time]
height = speed * speed / (2 * 9.805)

print("{} will launch the messenger {:.2f} meters high, ".format(contraption, round(height, 2)), end="")

if height > 50:
	print("OUCH!")
elif height > 25:
	print("SUCCESS!")
else:
	print("SPLAT!")
