def getMaximumEfficiency(capacity, numServers):
    n, m = len(capacity), len(numServers)    
    for i in range(n):
        for j in range(i+1,n):
            if capacity[i] > capacity[j]:
                capacity[i],capacity[j] = capacity[j], capacity[i]
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