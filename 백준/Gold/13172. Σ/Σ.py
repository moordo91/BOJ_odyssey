import sys
# from collections import deque
input = sys.stdin.readline

x = 10**9 + 7

def sol(a, b):
    if b == 1:
        return a % x
    elif b % 2:
        return a * sol(a, b - 1) % x
    else:
        p = sol(a, b // 2)
        return p * p % x

m = int(input())
ans = 0

for _ in range(m):
    n, s = map(int, input().split())
    ans += s * sol(n, x - 2) % x

print(ans % x)