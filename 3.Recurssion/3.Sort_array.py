def insert(element, sorted_arr):
    if not sorted_arr or element <= sorted_arr[0]:
        return [element] + sorted_arr
    return [sorted_arr[0]] + insert(element, sorted_arr[1:])


def sort_array(arr):
    if len(arr) <=1:
        return arr
    sorted_arr = sort_array(arr[1:])
    return insert(arr[0], sorted_arr)


if __name__ == "__main__":
    arr = [5, 2, 9, 1, 5, 6]
    sorted_arr = sort_array(arr)
    print(f"The sorted array is: {sorted_arr}")