# Number of subset we can create by adding + and - sign to get target sum
# Goal -- s1-s2=diff
def target_sum(arr,diff):
    total=sum(arr)
    target=(total-diff)//2
    if diff>total or (total-diff)%2!=0:
            return 0
    n=len(arr)
    dp=[[0 for i in range(target+1)] for j in range(n+1)]
    for i in range(n+1):
          dp[i][0]=1
    for i in range(1,n+1):
          for j in range(1,target+1):
                if arr[i-1]<=j:
                      dp[i][j]=dp[i-1][j]+dp[i-1][j-arr[i-1]]
                else:
                      dp[i][j]=dp[i-1][j]
    return dp[n][target]



if __name__ == "__main__":
    test_cases=[
        ([1,1,2,3],1,3),
        ([1,2,3,1],3,2),
        ([1,1,1,1],0,6), # choose 2 of the four 1's to balance: C(4,2)=6
    ]
    for arr,diff,expected in test_cases:
        result=target_sum(arr,diff)
        print(result,"expected:",expected)
    