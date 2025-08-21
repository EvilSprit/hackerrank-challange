def getMaximumEfficiency(capacity, numServers):
    n, m = len(capacity), len(numServers)    
    capacity.sort()    
    cnt, ans = 0, 0
    tot = 0
    l, r = 0, n - 1
    for x in numServers:
        tot += x
        if x == 1:
            cnt += 1
        else:
            ans += capacity[r] - capacity[l]
            l += 1
            r -= 1  
    return ans