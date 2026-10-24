# Given a list or array find the next greatest element to the right.
# If no greater element exists to the right, the answer is -1.
# Eg [1,3,2,4,5,9] -- output [3,4,4,5,9,-1]

def next_right(array):
    result = [-1] * len(array)
    stack = []  # values, kept in decreasing order from top to bottom

    for i in range(len(array) - 1, -1, -1):
        if not stack:
            result[i] = -1
        elif stack[-1] > array[i]:
            result[i] = stack[-1]
        else:
            while stack and stack[-1] <= array[i]:
                stack.pop()
            result[i] = stack[-1] if stack else -1

        stack.append(array[i])

    return result


if __name__ == "__main__":
    test_cases = [
        ([1, 3, 2, 4, 5, 9], [3, 4, 4, 5, 9, -1]),  # normal case
        ([4, 3, 2, 1], [-1, -1, -1, -1]),           # strictly decreasing
        ([1, 2, 3, 4], [2, 3, 4, -1]),               # strictly increasing
    ]

    for array, expected in test_cases:
        print(next_right(array), "expected:", expected)




# 1.Next_Gratest_to_Right → right-to-left ✓
# 2.Next_Gratest_to_left → left-to-right ✓
# 3.Next_Smaller_to_left → left-to-right ✓
# 4.Next_Smaller_to_Right → right-to-left ✓