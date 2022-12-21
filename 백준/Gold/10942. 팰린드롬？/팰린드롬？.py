import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    dp[i][i] = 1

for i in range(n-1):
    if arr[i] == arr[i+1]:
        dp[i][i+1] = 1
    
for i in range(n-2):
    for j in range(i, n-2):
        if arr[j-i] == arr[j+2] and dp[j-i+1][j+1]:
            dp[j-i][j+2] = 1
            
m = int(input())
for _ in range(m):
    s, e = map(int, input().split())
    s, e = s-1, e-1
    print(dp[s][e])