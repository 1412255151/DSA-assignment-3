from collections import deque

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

def bfs_traversal(root):
    if not root:
        return
    
    queue = deque()
    queue.append(root)
    while queue:
        node = queue.popleft()
        print(node.value, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

def dfs_traversal(node):
    if not node:
        return
    print(node.value, end=" ")
    dfs_traversal(node.left)
    dfs_traversal(node.right)


print("Build the binary tree:")
root = build_binary_tree()


print("\nBFS Traversal:")
bfs_traversal(root)


print("\nDFS Traversal:")
dfs_traversal(root)