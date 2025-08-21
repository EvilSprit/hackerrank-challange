from bisect import bisect_right

def findMissingInteger(arr, k):
    s = set(arr)
    a = sorted(s)
    l = 1
    r = 2 * 10**12

    while l <= r:
        mid = (l + r) // 2
        index = bisect_right(a, mid)
        temp = mid - index

        if temp == k:
            return mid
        if temp > k:
            r = mid - 1
        else:
            l = mid + 1

    return 0