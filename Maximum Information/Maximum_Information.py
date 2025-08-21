def gainMaxValue(security_val, k):
    n = len(security_val)
    dp = [-10**18] * (n + 1)
    for i in range(n-1, -1, -1):
        max_value_from_i = security_val[i]
        if i + k < n:
            max_value_from_i += dp[i+k]
        dp[i] = max_value_from_i
    return max(dp[0:])