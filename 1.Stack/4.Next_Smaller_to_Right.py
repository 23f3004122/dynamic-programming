def next_smaller_to_right(arr):
    result=[-1]*len(arr)
    stack=[]
    for i in range(len(arr)-1,-1,-1):
        while stack and stack[-1]>=arr[i]:
            stack.pop()
        result[i]=stack[-1] if stack else -1
        stack.append(arr[i])
    return result

if __name__=="__main__":
    test_cases=[
        ([1,3,2,4,5,9],[-1,2,-1,-1,-1,-1]), #normal case
        ([4,3,2,1],[3,2,1,-1]),       #strictly decreasing
        ([1,2,3,4],[-1,-1,-1,-1]),          #strictly increasing
    ]
    for array,expected in test_cases:
        print(next_smaller_to_right(array),"expected:",expected)
