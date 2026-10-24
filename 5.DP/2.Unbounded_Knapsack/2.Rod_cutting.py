def rod_cutting(price_arr,size_arr,n):
    dp=[[0 for i in range(n+1)] for j in range(len(price_arr)+1)]
    for i in range(1,len(price_arr)+1):
        for j in range(1,n+1):
            if size_arr[i-1]<=j:
                dp[i][j]=max(dp[i-1][j],price_arr[i-1]+dp[i][j-size_arr[i-1]])
            else:
                dp[i][j]=dp[i-1][j]
    return dp[len(price_arr)][n]