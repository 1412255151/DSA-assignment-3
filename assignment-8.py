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

def count_subtrees_with_sum(node, x, count):
    if node is None:
        return 0
    
    left_sum = count_subtrees_with_sum(node.left, x, count)
    right_sum = count_subtrees_with_sum(node.right, x, count)
    total_sum = left_sum + right_sum + node.value
    
    if total_sum == x:
        count[0] += 1
    
    return total_sum


print("Build the binary tree:")
root = build_binary_tree()


x = int(input("Enter the target sum (x): "))


count = [0] 
count_subtrees_with_sum(root, x, count)
print("Number of subtrees with sum equal to", x, "is", count[0])