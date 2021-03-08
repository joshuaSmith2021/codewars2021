import math
import sys

def calc(h, r):
    print('{0:.2f} cubic inches'.format(math.pi * r * r * h))


for line in sys.stdin.read().splitlines():
    h, r = map(float, line.split())
    calc(h, r)
