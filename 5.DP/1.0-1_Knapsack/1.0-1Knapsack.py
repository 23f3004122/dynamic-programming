def knapsack(Warray,ValArray, W, n):
    if n==0 or W==0:
        return 0
    if Warray[n-1]>W:
        return knapsack(Warray, ValArray, W, n-1)
    else:
        return max(ValArray[n-1]+knapsack(Warray, ValArray, W-Warray[n-1], n-1), knapsack(Warray, ValArray, W, n-1))



if __name__ == "__main__":
    Warray=[1,2,3,4,5]
    ValArray=[1,6,10,16,20]
    W=7
    n=len(Warray)
    result=knapsack(Warray, ValArray, W, n)
    print(f"The maximum value in the knapsack is: {result}")