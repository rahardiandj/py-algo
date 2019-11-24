class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data


root = Node(99)
root.left = Node("00")
root.right = Node("A")
root.left.left = Node("B")
root.left.right = Node("C")



def preorder_print(root, s):
    result = ''

    traverse_root = root

    for elem in s :
        traverse_root = traverse_root.left if elem == "0" else traverse_root.right
            
        if traverse_root.left == None and traverse_root.right == None:
            result = result + traverse_root.data
            traverse_root = root

    print(result)

s="1001011"
preorder_print(root, s)
