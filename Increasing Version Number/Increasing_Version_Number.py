def getMinimumOperations(versionNumbers):
    n = len(versionNumbers)
    pre = 0
    out = 0

    for i in range(n):
        if versionNumbers[i] <= pre:
            add = (pre + 1 - versionNumbers[i] + i) // (i + 1)
            out += add
            pre = versionNumbers[i] + add * (i + 1)
        else:
            pre = versionNumbers[i]

    return out