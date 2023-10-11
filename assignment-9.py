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

def max_level_sum(root):
    if not root:
        return 0
    
    max_sum = float('-inf')
    level = 1
    queue = [root]
    
    while queue:
        level_sum = sum(node.value for node in queue)
        if level_sum > max_sum:
            max_sum = level_sum
            max_level = level
        
        temp_queue = []
        for node in queue:
            if node.left:
                temp_queue.append(node.left)
            if node.right:
                temp_queue.append(node.right)
        queue = temp_queue
        level += 1
    
    return max_level, max_sum


print("Build the binary tree:")
root = build_binary_tree()

max_level, max_sum = max_level_sum(root)
print("Level with maximum sum:", max_level)
print("Maximum sum at this level:", max_sum)