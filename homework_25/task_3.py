class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, item):
        new_node = Node(item)

        if self.front is None:
            self.front = self.rear = new_node
            return

        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            raise ValueError("Queue is empty")

        value = self.front.data
        self.front = self.front.next

        if self.rear is None:
            self.rear = None

        return value

    def peek(self):
        if self.front is None:
            return None
        return self.front.data

    def is_empty(self):
        return self.front is None