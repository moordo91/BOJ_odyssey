import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))
t, p = map(int, input().split())

a = 0
for i in s:
    tmp = i // t
    if i % t != 0:
        tmp += 1
    a += tmp

b, c = n // p, n % p
print(a)
print(b, c)