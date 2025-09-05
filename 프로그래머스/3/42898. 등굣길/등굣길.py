
def solution(m, n, puddles):
    answer = 0
    dp = [[0] * (m+1) for _ in range(n+1)]
    for x, y in puddles:
        dp[y][x] = -1
    
    
    dp[1][1] = 1
    
    for y in range(1, n+1):
        for x in range(1, m+1):
            if dp[y][x] == -1:
                continue
            
            if dp[y-1][x] != -1:
                dp[y][x] += dp[y-1][x]
            if dp[y][x-1] != -1:
                dp[y][x] += dp[y][x-1]
                
            dp[y][x] %= 1000000007
            
    answer = dp[n][m]
    return answer