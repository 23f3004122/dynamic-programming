def longest_repeating_subsequence(s):
    n = len(s)
    # Create a 2D array to store lengths of longest repeating subsequence
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    # Build the dp array
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s[i - 1] == s[j - 1] and i != j:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][n]
    

if __name__ == "__main__":
    s = "AABEBCDD"
    print(longest_repeating_subsequence(s))  # Output: 3 (The longest repeating subsequence is "ABD")

    