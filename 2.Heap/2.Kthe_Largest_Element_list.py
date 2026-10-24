import heapq
def kth_largest_element_list(array, k):
    heap=[]
    for num in array:
        heapq.heappush(heap,num)
        if len(heap)>k:
            heapq.heappop(heap)
    return heap 


if __name__ == "__main__":
    array = [7, 10, 4, 3, 20, 15]
    k = 3

    result = kth_largest_element_list(array, k)

    print(f"The {k}th largest element is: {result}")
       