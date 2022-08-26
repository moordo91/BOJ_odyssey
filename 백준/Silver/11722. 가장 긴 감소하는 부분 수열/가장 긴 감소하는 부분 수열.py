n = int(input())
dp = [0 for _ in range(n)]
arr = list(map(int, input().split()))

for i in range(n):
    for j in range(i):
        if arr[i] < arr[j] and dp[i] < dp[j]:
            dp[i] += 1
    dp[i] += 1

print(max(dp))