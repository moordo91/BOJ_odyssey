n = int(input())
arr = list(map(int, input().split()))
dp = arr.copy()

for i in range(1, n):
    for j in range(i-1, 0-1, -1):
        if arr[j] < arr[i] and dp[i] < dp[j] + arr[i]:
            dp[i] = dp[j] + arr[i]

print(max(dp))