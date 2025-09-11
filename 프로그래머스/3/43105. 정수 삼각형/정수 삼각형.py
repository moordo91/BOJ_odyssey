def solution(triangle):
    n = len(triangle)
    m = 1
    dp = [[0] * i for i in range(1, n+1)]
    dp[0][0] = triangle[0][0]
    
    for i in range(1, n):
        for j in range(i+1):
            if j == 0:
                x = dp[i-1][j]
            elif j == i:
                x = dp[i-1][j-1]
            else:
                x = max(dp[i-1][j-1], dp[i-1][j])
            dp[i][j] = x + triangle[i][j] 
    
    answer = max(dp[n-1])
    return answer