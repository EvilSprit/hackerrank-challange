long getMinimumOperations(vector<int> versionNumbers) {
    int n = versionNumbers.size();
    assert(n >= 1 and n <= 2e5);
    for (auto x: versionNumbers)   assert(x >= 1 and x <= 1e9);
        
    long ans = 0, lst = versionNumbers[0];
    for(int i = 1; i < n; i++) {
        if (lst < versionNumbers[i]) {
            lst = versionNumbers[i];
            continue;
        }
        
        long x = ((lst - versionNumbers[i]) / (i + 1)) + 1;
        ans += x, lst = versionNumbers[i] + (i + 1) * x;
    }
    return ans;
}