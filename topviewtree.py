class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def traverse(root):
    result = []
    if (root):
        result = traverse(root.left)
        result.append(root.data)
        result = result + traverse(root.right)
        
    return result

def post_traverse(root):
    result = []
    if (root):
        # result = traverse(root.left)
        result = result + traverse(root.right)
        result.append(root.data)
        
    return result



root = Node(1)
root.left = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right = Node(5)
root.right.left = Node(6)

print(traverse(root))
print(post_traverse(root))

