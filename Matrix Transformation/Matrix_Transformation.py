def getOriginalArray(mat):
    n = len(mat)
    
    sum_of_matrix = sum(map(sum, mat))    
    sum_of_arr = sum_of_matrix // (3 * n - 3)
    
    arr = [(sum(mat[i]) - sum_of_arr) // (2 * n - 3) for i in range(n)]
    
    return arr