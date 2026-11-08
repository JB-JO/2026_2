class Node:
    def __init__(self, data,link=None):
        self.data = data
        self.link = link

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self): return self.head is None
    def is_full(self): return False

    def get_node(self, pos):
        if pos < 0: return None
        node = self.head
        while pos > 0 and node is not None:
            node = node.link
            pos -= 1
        return node

    def get_entry(self, pos):
        node = self.get_node(pos)
        if node is None : return None
        else : return node.data

    def insert(self, pos, data):
        before = self.get_node(pos - 1)
        if before is None:
            self.head =  Node(data, self.head)
        else:
            node = Node(data, before.link)
            before.link = node

    def delete(self, pos):
        before = self.get_node(pos - 1)
        if before is None:
            if self.head is not None:
                self.head = self.head.link
        elif before.link is not None:
            before.link = before.link.link

    def size(self):
        node = self.head
        count = 0
        while not node is None:
            node = node.link
            count += 1
        return count

    def __str__(self):
        arr  = []
        node = self.head
        while node is not None:
            arr.append(node.data)
            node = node.link
        return str(arr)

    def print_forward(self):
        node = self.head
        print("List : ", end="")
        while node is not None:
            print(f"{node.data}", end=" -> "if node.link else"")
            node = node.link
        print()

    def print_reverse(self):
        arr = []
        node = self.head
        print("Reverse List : ", end="")
        while node is not None:
            arr.append(node.data)
            node = node.link
        for i in range(len(arr) - 1, -1, -1): #파이썬 range에서는 (시작값, 끝값"경계", 증감값)으로 증감이 1이면 생략가능.
            print(f"{arr[i]}", end=" -> ")
        print()

    def append(self, data):
        node = Node(data, None)
        if self.head is None:
            self.head = node
        else:
            tail = self.head
            while tail.link is not None:
                tail = tail.link
            tail.link = node

    def merge(self, other):
        if other.is_empty():
            pass
        elif self.is_empty():
            self.head = other.head
            other.head = None
        else:
            tail = self.head
            while tail.link is not None:
                tail = tail.link
            tail.link = other.head
            other.head = None

