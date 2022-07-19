import sys; gets = sys.stdin.readline

t = int(gets())
for _ in range(t):
    a, b = map(int, gets().split())
    print(1 if b % a == 0 and b != a else 0)