import sys

def number(x):
    if '/' in x:
        num, den = map(float, x.split('/'))
        return num / den
    else:
        return float(x)

def line_check(line):
    stick_count, stick_size, tolerance = map(number, line.split())
    total_sticks = stick_count * stick_size
    total_mj = total_sticks * 0.45 * 7.5
    print('{0:.2f} the Mask {1} eat it!'.format(total_mj, 'can' if tolerance > total_mj else 'should not'))


for line in sys.stdin.read().splitlines():
    line_check(line)
