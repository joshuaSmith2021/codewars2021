import sys

line = sys.stdin.read().splitlines()[0]

height, y, power = map(float, line.split())

if power < 10 or y > height:
    for i in range(height):
        print('#')
