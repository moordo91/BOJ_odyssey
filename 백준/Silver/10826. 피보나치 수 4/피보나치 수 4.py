dp = [0, 1] + [0] * 10_000

def fib(x, dp):
    for i in range(2, x+1):
        dp[i] = dp[i-1] + dp[i-2]

x = int(input())
fib(x, dp)
print(dp[x])
