def Next_smaller_to_left(array):
    stack=[]
    result=[-1]*len(array)
    for i in range(0,len(array),1):
        while stack and stack[-1]>=array[i]:
            stack.pop()
        result[i]=stack[-1] if stack else -1
        stack.append(array[-1])

    return result

if __name__ == "__main__":
    test_cases=[
        ([1,3,2,4,5,9],[-1,1,1,2,4,5]), #normal case
        ([4,3,2,1],[-1,-1,-1,-1]),       #strictly decreasing
        ([1,2,3,4],[-1,1,2,3]),       #strictly increasing
    ]
    for array,expected in test_cases:
        print(Next_smaller_to_left(array),"expected:",expected)