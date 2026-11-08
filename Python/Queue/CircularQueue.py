class CircularQueue:
        def __init__(self, capacity = 10):
            self.capacity = capacity
            self.array = [None] * capacity
            self.front = 0
            self.rear = 0

        def is_empty(self):
            return self.front == self.rear

        def is_full(self):
            return self.front == (self.rear + 1) % self.capacity

        def enqueue(self, data):
            if not self.is_full():
                self.rear = (self.rear + 1) % self.capacity
                self.array[self.rear] = data
            else : pass

        def dequeue(self):
            if not self.is_empty():
                self.front = (self.front + 1) % self.capacity
                return self.array[self.front]
            else : pass

        def peek(self):
            if not self.is_empty():
                return self.array[(self.front + 1) % self.capacity]
            else : pass

        def size(self):
            return (self.rear - self.front + 1) % self.capacity

        def clear(self):
            self.array = [None] * self.capacity
            self.front = 0
            self.rear = 0

        def __str__(self):
            if self.front < self.rear:
                return str(self.array[self.front + 1: self.rear + 1])
            else:
                return str(self.array[self.front + 1 : self.capacity] + \
                           self.array[0:self.rear + 1])