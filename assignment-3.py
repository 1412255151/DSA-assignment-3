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

def preorder_traversal(node):
    if node:
        print(node.value, end=" ")
        preorder_traversal(node.left)
        preorder_traversal(node.right)

def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.value, end=" ")
        inorder_traversal(node.right)

def postorder_traversal(node):
    if node:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.value, end=" ")

# Build the binary tree
print("Build the binary tree:")
root = build_binary_tree()

# Perform traversals
if root:
    print("\nPre-order traversal:")
    preorder_traversal(root)

    print("\nIn-order traversal:")
    inorder_traversal(root)

    print("\nPost-order traversal:")
    postorder_traversal(root)
else:
    print("Binary tree is empty.")