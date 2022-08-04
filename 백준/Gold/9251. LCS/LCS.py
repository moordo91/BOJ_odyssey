str1 = [None] + list(input())
str2 = [None] + list(input())
n, m = len(str1), len(str2)

dp = [[0 for _ in range(m)] for _ in range(n)]

for i in range(1, n):
    for j in range(1, m):
        if str1[i] == str2[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])