class DNode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DubleLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def is_full(self):
        return False

    def

