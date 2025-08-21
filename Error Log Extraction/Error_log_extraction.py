def extractErrorLogs(logs):
    n = len(logs)

    ans = []
    
    for i in range(n):
        dd, mm, yy = logs[i][0].split('-')
        hh, mn = logs[i][1].split(':')
        logs[i][0] = f"{yy}-{mm}-{dd}"
        
        if logs[i][2] == "CRITICAL" or logs[i][2] == "ERROR":
            ans.append([logs[i][0], logs[i][1], i, logs[i][2], logs[i][3]])

    ans.sort()
    
    for i in range(len(ans)):
        ans[i] = [ans[i][0],ans[i][1], ans[i][3],ans[i][4]]
        yy, mm, dd = ans[i][0].split('-')
        ans[i][0] = f"{dd}-{mm}-{yy}"

    return ans