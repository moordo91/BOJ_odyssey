import sys

input()
for line in sys.stdin:
    a, b = map(int, line.split())
    print(0 if b % a or a == b else 1)