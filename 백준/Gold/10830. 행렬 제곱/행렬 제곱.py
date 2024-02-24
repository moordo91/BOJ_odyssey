import sys
# from collections import deque
input = sys.stdin.readline

n, b = map(int, input().split())

mat = [list(map(int, input().split())) for _ in range(n)]

def matmul(x, y):
    global n
    result = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += x[i][k]*y[k][j] % 1000
    return result

def dnc(a, b):
    if b == 1:
        return a
    mat = dnc(a, b//2)
    if b % 2:
        return matmul(matmul(mat, mat), a)
    else:
        return matmul(mat, mat)
        
mat = dnc(mat, b)
for i in range(n):
    for j in range(n):
        mat[i][j] %= 1000

for i in range(n):
    for j in range(n):
        print(mat[i][j], end=' ')
    print()
