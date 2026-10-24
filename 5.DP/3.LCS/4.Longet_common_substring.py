def longest_common_substring(str1, str2):
    m = len(str1)
    n = len(str2)
    result = 0
    end = 0
    length = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                length[i][j] = length[i - 1][j - 1] + 1
                if length[i][j] > result:
                    result = length[i][j]
                    end = i
            else:
                length[i][j] = 0

    return str1[end - result:end]

if __name__ == "__main__":
    str1 = "ABABC"
    str2 = "BABCA"
    print(longest_common_substring(str1, str2))  # Output: "BABC"