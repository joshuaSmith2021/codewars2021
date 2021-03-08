import datetime
import sys

DINNERTIME = datetime.datetime(2021, 3, 6, 17)

def parse_time(string):
    hour, minute = map(int, string.split(':'))
    return datetime.datetime(2021, 3, 6, hour, minute)

snacks = []
for line in sys.stdin.read().splitlines():
    if line == 'END':
        break

    vid, app, vpf = line.split()
    prot_end = parse_time(app) + datetime.timedelta(minutes=float(vpf) * 10)
    if prot_end < DINNERTIME:
        snacks.append(vid.split('-')[1])

if len(snacks) == 0:
    print('Blah, blah, blah, time to order delivery')
else:
    print('Villagers ({0}) look tasty'.format(', '.join(snacks)))
