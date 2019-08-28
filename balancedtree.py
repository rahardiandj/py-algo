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

    if root == None :
        return True

    lh = height(root.left)
    rh = height(root.right)

    if abs(lh - rh) <= 0 and is_balanced(root.left) and is_balanced(root.right) :
        return True

    return False
    

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.right = Node(4)

# root.left.left = Node(4)
# root.left.right = Node(5)


tree_height = height(root)

# print("Height of tree ", tree_height)

print("Is balanced : ", is_balanced(root))