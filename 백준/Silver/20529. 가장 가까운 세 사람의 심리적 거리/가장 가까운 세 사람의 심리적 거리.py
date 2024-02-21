import sys
from collections import deque
input = sys.stdin.readline


def sumbiti(a, b):
    result = 0
    for i in range(4):
        if a[i] != b[i]:
            result += 1
    return result

t = int(input())


for _ in range(t):

    n = int(input())
    arr = list(map(str, input().split()))
    
    if n > 32:
        print(0)
    else:    
        result = 0
        min_result = 1e9
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    result += sumbiti(arr[i], arr[j])
                    result += sumbiti(arr[i], arr[k])
                    result += sumbiti(arr[j], arr[k])
                    min_result = min(min_result, result)
                    result = 0

        print(min_result)