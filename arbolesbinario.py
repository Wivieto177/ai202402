class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.data)
        inorder_traversal(root.right)

# Ejemplo de uso
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
inorder_traversal(root)  # Salida: 2 1 3
