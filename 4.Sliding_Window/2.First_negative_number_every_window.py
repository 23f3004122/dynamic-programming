def First_negative_number_every_window(arr, k):

    result = []
    q = []
    i=0

    for j in range(len(arr)):
        if j-i+1 < k:
            if arr[j]<0:
                q.append(arr[j])
        elif j-i+1 == k:
            if arr[j]<0:
                q.append(arr[j])
            if len(q)==0:
                result.append(0)
            else:
                result.append(q[0])
            if arr[i]<0:
                q.pop(0)
            i+=1
    return result

if __name__ == "__main__":
    arr = [12, -1, -7, 8, -15, 30, 16, 28]
    k = 3
    result = First_negative_number_every_window(arr, k)
    print(f"The first negative number in every window of size {k} is: {result}")
