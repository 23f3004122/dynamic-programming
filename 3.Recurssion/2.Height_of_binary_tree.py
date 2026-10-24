def height_of_binary_tree(node):
    if node is None:
        return 0
    else:
        left_height = height_of_binary_tree(node.left)
        right_height = height_of_binary_tree(node.right)
        return max(left_height, right_height) + 1