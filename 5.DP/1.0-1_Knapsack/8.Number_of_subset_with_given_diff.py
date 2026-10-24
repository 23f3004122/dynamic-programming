def Number_of_subset_with_given_diff(arr,diff):
    # sub1 - sub2 = diff
    # sub1+sub2=sum(arr)
    # it means 2*sub2=sum(arr)-diff
    total=sum(arr)
    if diff>total or (total-diff)%2!=0:
        return 0
    number=(total - diff)//2
    n=len(arr)
    dp=[[0 for i in range(number+1)] for j in range(n+1)]
    for i in range(n+1):
        dp[i][0]=1
    for i in range(1,n+1):
        for j in range(1,number+1):
            if arr[i-1]<=j:
                dp[i][j]=dp[i-1][j]+dp[i-1][j-arr[i-1]]
            else:
                dp[i][j]=dp[i-1][j]
    return dp[n][number]


if __name__ == "__main__":
    test_cases=[
        ([1,1,2,3],1,3),
        ([1,2,3,1],3,2),
        ([1,1,1,1],0,6), # choose 2 of the four 1's to balance: C(4,2)=6
    ]
    for arr,diff,expected in test_cases:
        result=Number_of_subset_with_given_diff(arr,diff)
        print(result,"expected:",expected)
