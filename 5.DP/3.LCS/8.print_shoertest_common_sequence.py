def shortest_common_supersequence(X, Y):
    m = len(X)
    n = len(Y)

    # Create a DP table to store lengths of longest common subsequence
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstruct the shortest common supersequence from the DP table
    i, j = m, n
    scs = []

    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            scs.append(X[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            scs.append(X[i - 1])
            i -= 1
        else:
            scs.append(Y[j - 1])
            j -= 1

    # Add remaining characters of X or Y
    while i > 0:
        scs.append(X[i - 1])
        i -= 1
    while j > 0:
        scs.append(Y[j - 1])
        j -= 1

    # The SCS is constructed in reverse order, so reverse it before returning
    return ''.join(reversed(scs))

if __name__ == "__main__":
    X = "AGGTAB"
    Y = "GXTXAYB"
    print(shortest_common_supersequence(X, Y))  # Output: "AGXGTXAYB"