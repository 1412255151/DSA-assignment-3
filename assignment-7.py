def calculate_sum_of_perfect_binary_tree(height):
    num_nodes = 2 ** height - 1
    first_term = 1
    last_term = 2 ** height - 1
    total_sum = (num_nodes / 2) * (first_term + last_term)
    return int(total_sum)


height = int(input("Enter the height of the perfect binary tree: "))


sum_of_nodes = calculate_sum_of_perfect_binary_tree(height)
print("Sum of all nodes in the perfect binary tree:", sum_of_nodes)