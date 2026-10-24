def trap(array):
    n = len(array)
    left_max = [0] * n
    right_max = [0] * n
    water_trapped = 0

    # Fill left_max array
    left_max[0] = array[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], array[i])

    # Fill right_max array
    right_max[n - 1] = array[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], array[i])

    # Calculate water trapped
    for i in range(n):
        water_trapped += min(left_max[i], right_max[i]) - array[i]

    return water_trapped

if __name__ == "__main__":
    test_cases = [
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),  # normal case
        ([4, 2, 0, 3, 2, 5], 9),                    # mixed heights
        ([1, 2, 3, 4], 0),                          # strictly increasing
        ([4, 3, 2, 1], 0),                          # strictly decreasing
    ]
    for array, expected in test_cases:
        print(trap(array), "expected:", expected)