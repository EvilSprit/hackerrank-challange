def maximumPoints(k, costs):
    # Write your code here

    mx = 0
    summ = 0
    ans = 0
    
    if sum(costs) <= k:
        return len(costs)
    
    for idx, val in enumerate(costs):
        mx = max(mx, val)
        summ += val
        if summ - mx <= k:
            ans  = idx

    return ans