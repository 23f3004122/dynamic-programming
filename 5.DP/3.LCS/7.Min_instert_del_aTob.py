def min_number_of_insertions_deletions(str1, str2):
    m = len(str1)
    n = len(str2)
    
    # Create a DP table to store lengths of longest common subsequence
    dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
    
    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # Length of longest common subsequence
    lcs_length = dp[m][n]
    
    # Minimum insertions and deletions
    min_insertions = n - lcs_length
    min_deletions = m - lcs_length
    
    return min_insertions, min_deletions