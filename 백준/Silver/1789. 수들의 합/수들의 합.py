import sys
# from collections import deque
input = sys.stdin.readline

n = int(input())

def check(x, n):
    a = n*(n+1)//2
    b = (n+1)*(n+2)//2
    if a <= x < b:
        return True
    else:
        return False

i = 1
while True:
    if check(n, i):
        print(i)
        break
    i += 1