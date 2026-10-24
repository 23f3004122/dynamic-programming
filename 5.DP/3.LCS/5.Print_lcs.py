def print_lcs(str1, str2):
    m = len(str1)
    n = len(str2)
    dp = [[0 for j in range(n + 1)] for i in range(m + 1)]

    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    i,j=m,n
    lcs_str=""
    while i>0 and j>0:
        if str1[i-1]==str2[j-1]:
            lcs_str+=str1[i-1]
            i-=1
            j-=1
        elif dp[i-1][j]>dp[i][j-1]:
            i-=1
        else:
            j-=1
    return lcs_str[::-1]

if __name__=="__main__":
    str1 = "AGGTAB"
    str2 = "GXTXAYB"
    print(print_lcs(str1, str2))  # Output: "GTAB"