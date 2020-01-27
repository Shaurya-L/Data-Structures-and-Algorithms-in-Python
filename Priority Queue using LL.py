class Node:
    def __init__(self, item, priority):
        self.item = item
        self.next = None
        self.priority = priority

class PriorityQueue:
    def __init__(self):
        self.front = self.rear = None

    def isEmpty(self):
        return self.front == None

    def enqueue(self, item, priority):
        newNode = Node(item, priority)
        if not self.rear:
            self.front = self.rear = newNode
            return
        if self.front.priority < newNode.priority:
            newNode.next = self.front
            self.front = newNode
            return
        previous = None
        current = self.front
        while(current and newNode.priority < current.priority):
            previous = current
            current = current.next
        if current:
            previous.next = newNode
            newNode.next = current
        else:
            self.rear.next = newNode
            self.rear = newNode

    def dequeue(self):
        if self.isEmpty():
            #print('Queue is empty')
            return "Queue is empty"
        temp = self.front
        self.front = self.front.next
        if self.front == None:
            self.rear = None
        return temp.item

p = PriorityQueue()
print(p.dequeue())
p.enqueue(3, 3)
p.enqueue(7, 6)
p.enqueue(1, 1)
print(p.dequeue())
p.enqueue(8, 8)
p.enqueue(6, 6)
p.enqueue(2, 2)
print(p.dequeue())
