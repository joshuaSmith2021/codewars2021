import sys

hookes = {
    'X': None,
    'F': None,
    'K': None
}

for line in sys.stdin.read().splitlines():
    var, val = line.split()

    if val == '?':
        continue

    hookes[var] = float(val)

def solve():
    if hookes['X'] is None:
        return -1 * hookes['F'] / hookes['K']
    elif hookes['F'] is None:
        return -1 * hookes['K'] * hookes['X']
    elif hookes['K'] is None:
        return -1 * hookes['F'] / hookes['X']

target = [x for x in hookes.keys() if hookes[x] is None][0]
print('{0} {1:.2f}'.format(target, solve()))
