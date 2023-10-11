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

def print_odd_level_nodes(root, level=1):
    if not root:
        return
    
    if level % 2 != 0:
        print(root.value, end=" ")
    
    print_odd_level_nodes(root.left, level + 1)
    print_odd_level_nodes(root.right, level + 1)


print("Build the binary tree:")
root = build_binary_tree()


print("\nNodes at odd levels:")
print_odd_level_nodes(root)