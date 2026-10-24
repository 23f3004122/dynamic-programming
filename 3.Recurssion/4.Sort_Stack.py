

def insert_in_sorted_order(stack, element):
    if not stack or element <= stack[0]:
        return [element] + stack
    return [stack[0]] + insert_in_sorted_order(stack[1:], element)


def sort_stack(stack):
    if not stack:
        return []

    top_element = stack.pop()
    sorted_stack = sort_stack(stack)
    return insert_in_sorted_order(sorted_stack, top_element)


if __name__ == "__main__":
    stack = [34, 3, 31, 98, 92, 23]
    sorted_stack = sort_stack(stack)
    print(f"The sorted stack is: {sorted_stack}")