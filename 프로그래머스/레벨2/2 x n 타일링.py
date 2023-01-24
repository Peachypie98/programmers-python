def solution(n):
    dp = [0]*60000
    dp[0] = 0
    dp[1] = 1
    for i in range(1, n+1):
        dp[i+1] = dp[i] % 1000000007 + dp[i-1] % 1000000007
    return dp[n+1] % 1000000007