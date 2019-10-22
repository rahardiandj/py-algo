class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def travese_list(self):
        if self.head == None :
            print("LinkedList has no element")
        else:
            cur_node = self.head
            while cur_node is not None :
                print(cur_node.data)
                cur_node = cur_node.ref

    def insert(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

linkedList = LinkedList()


linkedList.insert(1)
linkedList.insert(2)
linkedList.travese_list()


        

