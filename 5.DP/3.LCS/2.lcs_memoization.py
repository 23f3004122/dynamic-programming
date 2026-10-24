# dp is a 2D array of size (m+1)*(n+1) initialized with -1 
def lcs_memoization(Array1,Array2,m,n,dp):
    if m==0 or n==0:
        return 0
    if dp[m][n]!=-1:
        return dp[m][n]
    if Array1[m-1]==Array2[n-1]:
        dp[m][n]=1+lcs_memoization(Array1,Array2,m-1,n-1,dp)
    else:
        dp[m][n]=max(lcs_memoization(Array1,Array2,m,n-1,dp),lcs_memoization(Array1,Array2,m-1,n,dp))
    return dp[m][n]