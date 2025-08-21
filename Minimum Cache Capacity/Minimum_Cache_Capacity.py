from heapq import heappush, heappop

def getMinimumSize(requests, k):
    n = len(requests)
    lo, hi, ans = 1, n, -1

    while lo <= hi:
        mid = (lo + hi) // 2

        cnt = 0
        last = {}
        cache = []
        in_cache = {}
        hit = 0

        for x in requests:
            cnt += 1
            if in_cache.get(x, 0) == 1:
                hit += 1
                last[x] = cnt
                heappush(cache, [last[x], x])
            else:
                if len(in_cache) < mid:
                    in_cache[x] = 1
                    last[x] = cnt
                    heappush(cache, [last[x], x])
                else:
                    while len(cache) > 0 and cache[0][0] != last[cache[0][1]]:
                        heappop(cache)
                    in_cache[cache[0][1]] = 0
                    heappop(cache)
                    last[x] = cnt
                    in_cache[x] = 1
                    heappush(cache, [last[x], x])


        if hit >= k:
            ans = mid
            hi = mid - 1
        else:
            lo = mid + 1

    return ans