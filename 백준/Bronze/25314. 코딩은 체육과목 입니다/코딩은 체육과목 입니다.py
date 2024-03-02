import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
x = n // 4
if n % 4 != 0:
    x += 1
print("long " * x + "int")