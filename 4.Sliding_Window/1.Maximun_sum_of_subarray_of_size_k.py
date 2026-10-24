def maximu_sum_subarray(array,k):
    i=0 
    j=0 
    sum=0 
    max_result=0 
    while j<len(array):
        sum+=array[j]
        if (j-i+1) == k:
            max_result=max(max_result,sum)
            sum-=array[i]
            i+=1
        j+=1
    return max_result    

if __name__ == "__main__":
    array=[1,2,3,4,5,6,7,8,9]
    k=3
    result=maximu_sum_subarray(array,k)
    print(f"The maximum sum of subarray of size {k} is: {result}")