def stock_consicutive_days(prices):
    n = len(prices)
    result = [0] * n
    stack = []  # indices, prices decreasing bottom to top... top has smallest
    for i in range(n):
        while stack and prices[stack[-1]] <= prices[i]:
            stack.pop()
        result[i] = i - stack[-1] if stack else i + 1
        stack.append(i)
    return result


if __name__=="__main__":
    test_cases=[
        ([100,80,60,70,60,75,85],[1,1,1,2,1,4,6]), #normal case
        ([100,90,80,70],[1,1,1,1]),       #strictly decreasing
        ([10,20,30,40],[1,2,3,4]),          #strictly increasing
    ]
    for array,expected in test_cases:
        print(stock_consicutive_days(array),"expected:",expected)