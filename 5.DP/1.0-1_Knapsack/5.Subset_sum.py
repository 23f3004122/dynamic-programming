# def subset_sum(arr,sum):
#     n=len(arr)
#     if sum==0:
#         return True
#     if n==0:
#         return False
#     if arr[n-1]>sum:
#         return subset_sum(arr[:-1],sum)
#     else:
#         return subset_sum(arr[:-1],sum) or subset_sum(arr[:-1],sum-arr[n-1])


def subset_sum(arr,sum):
    n=len(arr)
    t=[[False for j in range(sum+1)] for i in range(n+1)]
    for i in range(n+1):
        t[i][0]=True
    for j in range(1,sum+1):
        t[0][j]=False
    for i in range(1,n+1):
        for j in range(1,sum+1):
            if arr[i-1]<=j:
                t[i][j]=t[i-1][j-arr[i-1]] or t[i-1][j]
            else:
                t[i][j]=t[i-1][j]
    return t[n][sum]





    


if __name__ == "__main__":
    arr=[2,3,7,8,10]
    target=11
    result=subset_sum(arr,target)
    print(f"A subset with sum {target} exists: {result}")