def Maximum_area_histogram(heights):
    left=[-1]*len(heights)
    right=[-1]*len(heights)
    stack=[]
    for i in range(len(heights)-1,-1,-1):
        while stack and heights[stack[-1]]>=heights[i]:
            stack.pop()
        right[i]=stack[-1] if stack else len(heights)
        stack.append(i)

    stack=[]
    for i in range(0,len(heights),1):
        while stack and heights[stack[-1]]>=heights[i]:
            stack.pop()
        left[i]=stack[-1] if stack else -1
        stack.append(i)
    return max([(right[i]-left[i]-1)*heights[i] for i in range(len(heights))])

if __name__=="__main__":
    test_cases=[
        ([1,3,2,4,5,9],12), #normal case
        ([4,3,2,1],4),       #strictly decreasing
        ([1,2,3,4],6),          #strictly increasing
    ]
    for array,expected in test_cases:
        print(Maximum_area_histogram(array),"expected:",expected)            