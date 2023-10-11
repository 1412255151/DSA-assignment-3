class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_binary_tree():
    value = input("Enter the value for the node (or type 'None' to skip): ")
    if value.lower() == "none":
        return None
    new_node = Node(int(value))
    new_node.left = build_binary_tree()
    new_node.right = build_binary_tree()
    return new_node

def sum_left_leaves(root, is_left=False):
    if not root:
        return 0
    
    if is_left and not root.left and not root.right:
        return root.value
    
    left_sum = sum_left_leaves(root.left, True)
    right_sum = sum_left_leaves(root.right, False)
    
    return left_sum + right_sum


print("Build the binary tree:")
root = build_binary_tree()


left_leaves_sum = sum_left_leaves(root)
print("Sum of all left leaves in the binary tree:", left_leaves_sum)