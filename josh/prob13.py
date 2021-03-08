import sys

lines = sys.stdin.read().splitlines()

vehicle = lines[0]
ramp_length, acc, width = map(float, lines[1:])

time = (2 * ramp_length / acc) ** 0.5
speed = time * acc
distance = (speed ** 2) / 9.805

def splash_check(distance, river):
    if distance < river - 5:
        return 'SPLASH'
    elif river - 5 <= distance <= river:
        return 'BARELY MADE IT'
    elif distance > river:
        return 'LIKE A BOSS'

print('{0} will reach a speed of {1:.2f} m/s on a {2:.0f} meter ramp, crossing {3:.1f} of {4:.1f} meters, {5}!'.format(vehicle, speed, ramp_length, distance, width, splash_check(distance, width)))
