class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def find_tree_height(node):
    if node is None:
        return -1  
    
    left_height = find_tree_height(node.left)
    right_height = find_tree_height(node.right)
    
    
    return max(left_height, right_height) + 1


def build_binary_tree():
    value = int(input("Enter the value for the node (or -1 to stop): "))
    if value == -1:
        return None
    
    node = Node(value)
    print(f"Enter left child of {value}:")
    node.left = build_binary_tree()
    print(f"Enter right child of {value}:")
    node.right = build_binary_tree()
    return node


if __name__ == "__main__":
    print("Enter values to build the binary tree:")
    root = build_binary_tree()

    
    height = find_tree_height(root)
    print("Height of the tree:", height)