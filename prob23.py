import sys

sizes = list(map(int, sys.stdin.read().splitlines()[1:]))

biggest = max(sizes)
line_width = biggest + (biggest + 1)

def print_line(string):
    padding = (line_width - len(string)) // 2
    print('{0}{1}{0}'.format(' ' * padding, string))


for size in sizes:
    print_line('#' * size)

    rows = []
    for i in range((size + 1) // 2):
        row = '#{0}#'.format(' ' * (size + i * 2))
        rows.append(row)

    for x in rows + rows[::-1][1:]:
        print_line(x)

    print_line('#' * size)
