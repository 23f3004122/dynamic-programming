def count_subset_with_sum(arr,sum):
    n=len(arr)
    dp=[[0 for i in range(sum+1)] for j in range(n+1)]
    for i in range(n+1):
        dp[i][0]=1
    for i in range(1,n+1):
        for j in range(1,sum+1):
            if arr[i-1]<=j:
                dp[i][j]=dp[i-1][j]+dp[i-1][j-arr[i-1]]
            else:
                dp[i][j]=dp[i-1][j]
    return dp[n][sum]


if __name__ == "__main__":
    test_cases=[
        ([1,2,3],3,2),      # subsets {3}, {1,2}
        ([1,1,2,3],4,3),    # subsets {1,3},{1,3},{1,1,2}
        ([2,3,5,6,8,10],10,3), # {2,8},{10},{2,3,5}
    ]
    for arr,target,expected in test_cases:
        result=count_subset_with_sum(arr,target)
        print(result,"expected:",expected)



