class Node:
    def __init__(self, data,link=None):
        self.data = data
        self.link = link

class LinkedCircularQueue:
    def __init__(self):
        self.tail = None

    def is_empty(self):
        return self.tail is None

    def is_full(self):
        return False

    def enqueue(self, item):
        node = Node(item, None)
        if self.is_empty():
            self.tail = node
            node.link = node
        else:
            node.link = self.tail.link
            self.tail.link = node
            self.tail = node

    def dequeue(self):
        if not self.is_empty():
            data = self.tail.link.data
            if self.tail.link is self.tail:
                self.tail = None
            else:
                self.tail.link = self.tail.link.link
            return data
        else:
            return None

    def size(self):
        if self.is_empty(): return 0
        else:
            count = 1
            node = self.tail.link
            while not node is self.tail:
                node = node.link
                count += 1
            return count

    def __str__(self):
        arr = []
        if not self.is_empty():
            node = self.tail.link
            while not node is self.tail:
                arr.append(node.data)
                node = node.link
            arr.append(node.data)
        return str(arr)
