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

def print_leaves(node):
    if node is None:
        return
    if node.left is None and node.right is None:
        print(node.value, end=" ")
    print_leaves(node.left)
    print_leaves(node.right)


print("Build the binary tree:")
root = build_binary_tree()


print("\nLeaf nodes in the binary tree:")
print_leaves(root)  