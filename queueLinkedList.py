class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None

    def enque(self, data):
        newNode = Node(data)
        if self.front is None:
            self.front = newNode
            return

        temp = self.front
        while temp.next:
            temp = temp.next

        temp.next = newNode

    def printQueue(self):
        if self.front is None:
            print("The queue is empty")
            return

        temp = self.front
        while temp:
            print(temp.data, end='->' if temp.next else '\n')
            temp = temp.next

    def dequeue(self):
        if self.front is None:
            print('The queue is empty')
            return

        next = self.front.next
        self.front = None
        self.front = next

    def preek(self):
        if self.front is None:
            print('The queue is empty')
            return

        print('The front of the queue is:', self.front.data)


queue = Queue()

queue.enque(15)
queue.enque(25)
queue.enque(35)
queue.enque(20)
queue.enque(10)

queue.printQueue()

queue.dequeue()

queue.printQueue()

queue.preek()
