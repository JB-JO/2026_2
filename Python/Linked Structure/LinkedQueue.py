class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link

class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def is_full(self):
        return False

    def enqueue(self, data):
        new_node = Node(data,None)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.link = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            node = self.front
            self.front = self.front.link
            return node.data

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.front.data

    def clear(self):
        self.front = None
        self.rear = None

    def size(self):
        count = 0
        if self.is_empty():
            return count
        else:
            node = self.front
            while node.link is not None:
                node = node.link
                count += 1
            return count

    def __str__(self):
        arr = []
        node = self.front
        if not self.is_empty():
            while node is not None:
                arr.append(node.data)
                node = node.link
        return str(arr)
