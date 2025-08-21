def getMinimumTime(requestedServers, transitionTime):
    n, m = len(requestedServers), len(transitionTime)
    pre = [0] * (m + 1)
    for i in range(m):
        pre[i + 1] = pre[i] + transitionTime[i]
    
    curr = 1
    ans = 0
    for x in requestedServers:
        if curr > x:
            ans += min(pre[m] - pre[curr - 1] + pre[x - 1], pre[curr] - pre[x])
        else:
            ans += min(pre[m] - pre[x] + pre[curr], pre[x - 1] - pre[curr - 1])
        curr = x
    return ans