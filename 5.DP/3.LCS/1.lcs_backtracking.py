def lcs(Array1,Array2,m,n):
    if m==0 or n==0:
        return 0
    if Array1[m-1]==Array2[n-1]:
        return 1+lcs(Array1,Array2,m-1,n-1)
    else:
        return max(lcs(Array1,Array2,m,n-1),lcs(Array1,Array2,m-1,n))


if __name__=="__main__":
    Array1="AGGTAB"
    Array2="GXTXAYB"
    m=len(Array1)
    n=len(Array2)
    print(lcs(Array1,Array2,m,n))    