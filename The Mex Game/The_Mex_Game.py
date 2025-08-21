def getMaximumMEX(arr):
    arr.sort()
    ans = 0
    for elem in arr:
        ans += (elem >= ans)
    return ans