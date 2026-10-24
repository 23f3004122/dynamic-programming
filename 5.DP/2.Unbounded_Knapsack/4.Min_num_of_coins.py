def Min_number_of_coins(coins, amount):
    n=len(coins)
    dp=[[0 for j in range(amount+1)] for i in range(n+1)]
    #Only initiazition of first row and first column is different from the previous problem
    for j in range(amount+1):
        dp[0][j]=float('inf')
    for i in range(1,n+1):
        for j in range(1,amount+1):
            if coins[i-1]<=j:
                dp[i][j]=min(dp[i][j-coins[i-1]]+1,dp[i-1][j])
            else:
                dp[i][j]=dp[i-1][j]
    
    return dp[n][amount]    

if __name__=="__main__":
    test_cases=[
        ([1,2,3],4,2),        # 2+2
        ([1,2,5],11,3),       # 5+5+1
        ([2],3,float('inf')), # unreachable
        ([1,3,4,5],7,2),      # 3+4
        ([1],0,0),            # zero amount needs zero coins
    ]
    for coins,amount,expected in test_cases:
        result=Min_number_of_coins(coins,amount)
        print(result,"expected:",expected)
