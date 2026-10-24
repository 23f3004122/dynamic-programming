def solve(stack,mid):
    if mid == 1:
        stack.pop()
        return
    element = stack.pop()
    solve(stack,mid-1)
    stack.append(element)
        
def delete_middle_element_stack(stack):
    if not stack:
        return []
    mid =len(stack)//2 + 1
    solve(stack,mid)
    return stack


if __name__ == "__main__":
    stack = [65, 78, 90, 12, 34, 56]
    updated_stack = delete_middle_element_stack(stack)
    print(f"The stack after deleting the middle element is: {updated_stack}")