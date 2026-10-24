# MAH -- Maximin area of Histogram
def MAH(Array):
    left=[-1]*len(Array)
    right=[-1]*len(Array)
    stack=[]
    for i in range(len(Array)-1,-1,-1):
        while stack and Array[stack[-1]]>=Array[i]:
            stack.pop()
        right[i]=stack[-1] if stack else len(Array)
        stack.append(i)

    stack=[]
    for i in range(0,len(Array),1):
        while stack and Array[stack[-1]]>=Array[i]:
            stack.pop()
        left[i]=stack[-1] if stack else -1
        stack.append(i)
    return max([(right[i]-left[i]-1)*Array[i] for i in range(len(Array))])

def max_area_rectangle_in_binary_matrix(matrix):
    array=[0]*len(matrix[0])
    array=[matrix[0][i] for i in range(len(matrix[0]))] 
    max_area=MAH(array)
    for i in range(1,len(matrix),1):
        for j in range(0,len(matrix[0]),1):
            if matrix[i][j]==0:
                array[j]=0
            else:
                array[j]+=matrix[i][j]
        max_area=max(max_area,MAH(array))
    return max_area


if __name__=="__main__":
    test_cases=[
        ([[0,1,1,0],[1,1,1,1],[1,1,1,0]],6), #normal case
        ([[0,0,0],[0,0,0],[0,0,0]],0),       #all zeros
        ([[1,1,1],[1,1,1],[1,1,1]],9),          #all ones
    ]
    for matrix,expected in test_cases:
        print(max_area_rectangle_in_binary_matrix(matrix),"expected:",expected)