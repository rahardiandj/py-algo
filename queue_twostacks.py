class Queue:
    def __init__(self):
        self.stack_en = []
        self.stack_de = []

    def enqueue(self, value):
        self.stack_en.append(value)
    
    def dequeue(self) :
        result = ''
        while self.stack_en:
            self.stack_de.append(self.stack_en.pop())
        
        result = self.stack_de.pop()

        while self.stack_de:
            self.stack_en.append(self.stack_de.pop())

        return result


q = Queue()

q.enqueue(1)
q.enqueue(2)

print(q.dequeue())

q.enqueue(3)
q.enqueue(4)

print(q.dequeue())

