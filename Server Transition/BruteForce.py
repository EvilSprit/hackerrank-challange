def sum_array(start, end, TT, m):
    pre = [0] * (m + 1)
    for i in range(m):
        pre[i + 1] = pre[i] + TT[i]
    return pre[end] - pre[start]

def getMinimumTime(requestedServers, transitionTime):
    n, m = len(requestedServers), len(transitionTime)
    curr = 1
    ans = 0
    
    for x in requestedServers:
        if curr > x:
            ans += min(sum_array(curr - 1, m, transitionTime, m) + sum_array(0, x - 1, transitionTime, m), 
                       sum_array(x, curr, transitionTime, m))
        else:
            ans += min(sum_array(x, m, transitionTime, m) + sum_array(0, curr, transitionTime, m), 
                       sum_array(curr - 1, x - 1, transitionTime, m))
        curr = x
    
    return ans