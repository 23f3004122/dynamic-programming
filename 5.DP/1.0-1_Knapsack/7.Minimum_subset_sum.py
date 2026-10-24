def Minimum_subset_sum(arr):
    def subset(arr,target):
        n=len(arr)
        dp=[[False for i in range(target+1)] for j in range(n+1)]
        for i in range(n+1):
            dp[i][0]=True
        for i in range(1,n+1):
            for j in range(1,target+1):
                if arr[i-1]<=j:
                    dp[i][j]=dp[i-1][j]  or dp[i-1][j-arr[i-1]]
                else:
                    dp[i][j]=dp[i-1][j]        
        return dp[n][target]            

    total=sum(arr)
    target=total//2
    for i in range(target,-1,-1):
        if subset(arr,i):
            return (total-2*i)


if __name__ == "__main__":
    test_cases=[
        ([1,6,11,5],1),
        ([1,2,3,9],3),
        ([5],5),
        ([],0),
    ]
    for arr,expected in test_cases:
        result=Minimum_subset_sum(arr)
        print(result,"expected:",expected)