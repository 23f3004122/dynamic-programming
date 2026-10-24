def lcs(Array1,Array2,m,n):
    dp=[[0 for j in range(n+1)] for i in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if Array1[i-1]==Array2[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i][j-1],dp[i-1][j])
    return dp[m][n]

if __name__=="__main__":
    Array1="AGGTAB"
    Array2="GXTXAYB"
    m=len(Array1)
    n=len(Array2)
    print(lcs(Array1,Array2,m,n))