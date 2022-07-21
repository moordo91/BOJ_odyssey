import math
import sys; gets = sys.stdin.readline

def sol(M, N, x, y):
    LCM = math.lcm(M, N)
    while LCM >= max(x, y):
        if x > y:
            y += N
        elif x < y:
            x += M
        else:
            return x
    return -1
        
for _ in range(int(input())):
    M, N, x, y = map(int, gets().split())
    print(sol(M, N, x, y))