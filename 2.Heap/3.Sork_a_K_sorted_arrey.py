
import heapq


def sort_k_sorted_array(arr, k):
    n = len(arr)
    heap = []
    result = []

    for i in range(min(k + 1, n)):
        heapq.heappush(heap, arr[i])

    for i in range(k + 1, n):
        result.append(heapq.heappop(heap))
        heapq.heappush(heap, arr[i])

    while heap:
        result.append(heapq.heappop(heap))

    return result

if __name__ == "__main__":
    arr = [6, 5, 3, 2, 8, 10, 9]
    k = 3

    sorted_array = sort_k_sorted_array(arr, k)

    print(f"The sorted array is: {sorted_array}")