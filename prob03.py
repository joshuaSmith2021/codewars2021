import sys

lines = sys.stdin.read().splitlines()

for i, line in enumerate(lines):
    if 'P' in line:
        x = line.index('P')
        print('Ace, move fast, pigeon is at ({0}, {1})'.format(x, i))
        exit()

print('No pigeon, try another map, Ace')
