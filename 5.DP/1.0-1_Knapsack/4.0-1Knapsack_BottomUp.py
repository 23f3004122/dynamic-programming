def knapsack(Warray,Varray,W,n):
    t=[[0 for w in range(W+1)] for i in range(n+1)]
    for i in range(1,n+1):
        for w in range(1,W+1):
            if Warray[i-1]<=w:
                t[i][w]=max(Varray[i-1]+t[i-1][w-Warray[i-1]], t[i-1][w])
            else:
                t[i][w]=t[i-1][w]
    return t[n][W]


if __name__ == "__main__":
    Warray=[1,2,3,4,5]
    Varray=[1,6,10,16,20]
    W=7
    n=len(Warray)
    result=knapsack(Warray,Varray,W,n)
    print(f"The maximum value in the knapsack is: {result}")
