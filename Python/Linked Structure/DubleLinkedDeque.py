class DNode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DubleLinkedDeque:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def is_full(self):
        return False

    def add_front(self, data):
        node = DNode(data, None, self.front)
        if self.is_empty():
            self.front = self.rear = node
        else:
            self.front.prev = node
            self.front = node

    def add_rear(self, data):
        node = DNode(data,self.rear,None)
        if self.is_full():
            self.rear = self.front = node
        else:
            self.rear.next = node
            self.rear = node

    def delete_front(self):
        if not self.is_empty():
            data = self.front.data
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            else:
                self.front.prev = None
            return data
        else:
            return None

    def delete_rear(self):
        if not self.is_empty():
            data = self.rear.data
            self.rear = self.rear.prev
            if self.rear is None:
                self.front = None
            else:
                self.rear.next =None
            return data
        else:
            return None

    def peek_front(self):
        if self.is_empty():
            return None
        else:
            return self.front.data

    def peek_rear(self):
        if self.is_empty():
            return None
        else:
            return self.rear.data

    def count(self):
        if self.is_empty():
            return 0
        else:
            node = self.front
            count = 0
            while node is not None:
                count += 1
                node = node.next
            return count

    def __str__(self):
        arr = []
        node = self.front
        while node is not None:
            arr.append(node.data)
            node = node.next
        return str(arr)
