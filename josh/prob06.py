import sys

plain  = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
cipher = 'FGHIJKLMNOPQRSTUVWXYZABCDE '

lines = sys.stdin.read().splitlines()
text = lines[1]

for char in text:
    print(plain[cipher.index(char)], end='')