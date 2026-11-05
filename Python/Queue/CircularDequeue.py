from CircularQueue import *

class CircularDequeue(CircularQueue):
    def __init__(self, capacity = 10):
        super().__init__(capacity)


    def add_rear(self, data):
        self.enqueue(data)

    def delete_front(self):
        return self.dequeue()

    def get_front(self):
        return self.peek()

    def add_front(self, data):
        if not self.is_full():
            self.array[self.front] = data
            self.front = (self.front - 1 + self.capacity) % self.capacity
        else: pass

    def delete_rear(self):
        if not self.is_empty():
            data = self.array[self.rear]
            self.array[self.rear] = None
            self.rear = (self.rear - 1 + self.capacity) % self.capacity
            return data
        else: pass

    def get_rear(self):
        if not self.is_empty():
            return self.array[self.rear]
        else : pass