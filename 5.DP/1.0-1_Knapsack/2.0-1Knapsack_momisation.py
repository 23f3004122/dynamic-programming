def knapsack(Warray,Varray,W,n,t=None):
    if t is None:
        t=[[-1 for j in range(W+1)] for i in range(n+1)]
    if n==0 or W==0:
        return 0
    if t[n][W]!=-1:
        return t[n][W]
    if Warray[n-1]>W:
        t[n][W]=knapsack(Warray,Varray,W,n-1,t)
        return t[n][W]
    else:
        t[n][W]=max(Varray[n-1]+knapsack(Warray,Varray,W-Warray[n-1],n-1,t),knapsack(Warray,Varray,W,n-1,t))
        return t[n][W]

if __name__ == "__main__":
    Warray=[1,2,3,4,5]
    Varray=[1,6,10,16,20]
    W=7
    n=len(Warray)
    result=knapsack(Warray,Varray,W,n)
    print(f"The maximum value in the knapsack is: {result}")
    