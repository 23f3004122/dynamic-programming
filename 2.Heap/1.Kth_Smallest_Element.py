import heapq


def kth_smallest_element(array, k):
    heap = []

    for num in array:
        heapq.heappush(heap, -num)

        if len(heap) > k:
            heapq.heappop(heap)

    return -heap[0]


if __name__ == "__main__":
    array = [7, 10, 4, 3, 20, 15]
    k = 3

    result = kth_smallest_element(array, k)

    print(f"The {k}th smallest element is: {result}")