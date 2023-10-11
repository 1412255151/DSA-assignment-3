class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)
    
    def _insert_recursive(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(node.left, key)
        elif key > node.val:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(node.right, key)
        
    
    def inorder_traversal(self):
        result = []
        self._inorder_traversal_recursive(self.root, result)
        return result
    
    def _inorder_traversal_recursive(self, node, result):
        if node:
            self._inorder_traversal_recursive(node.left, result)
            result.append(node.val)
            self._inorder_traversal_recursive(node.right, result)
    
    def preorder_traversal(self):
        result = []
        self._preorder_traversal_recursive(self.root, result)
        return result
    
    def _preorder_traversal_recursive(self, node, result):
        if node:
            result.append(node.val)
            self._preorder_traversal_recursive(node.left, result)
            self._preorder_traversal_recursive(node.right, result)
    
    def postorder_traversal(self):
        result = []
        self._postorder_traversal_recursive(self.root, result)
        return result
    
    def _postorder_traversal_recursive(self, node, result):
        if node:
            self._postorder_traversal_recursive(node.left, result)
            self._postorder_traversal_recursive(node.right, result)
            result.append(node.val)


if __name__ == "__main__":
    tree = BinaryTree()
    elements = list(map(int, input("Enter space-separated values for the binary tree: ").split()))
    for element in elements:
        tree.insert(element)

    print("In-order Traversal:", tree.inorder_traversal())
    print("Pre-order Traversal:", tree.preorder_traversal())
    print("Post-order Traversal:", tree.postorder_traversal())