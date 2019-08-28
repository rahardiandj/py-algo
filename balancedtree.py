class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def height(root):

    if root is None:
        return 0
    
    return max(height(root.right), height(root.left)) + 1


def is_balanced(root):
    

root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)


tree_height = height(root)

print("Height of tree ", tree_height)