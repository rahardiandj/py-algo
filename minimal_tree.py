from pprint import pprint

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def buildMinTree(arr, start, end):

    if end < start:
        return
    mid = (start + end) // 2    
    node = Node(arr[mid])

    node.left = buildMinTree(arr, start, mid -1)
    node.right =buildMinTree(arr, mid + 1, end)
    return node

arr = [1,2,4,5]
a = buildMinTree(arr, 0, len(arr)-1)

print(a)


