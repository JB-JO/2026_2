class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None]*self.capacity
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity-1

    def push(self, val):
        if not self.is_full():
            self.top += 1
            self.array[self.top] = val
        else: pass

    def pop(self):
        if not self.is_empty():
            self.top -= 1
            return self.array[self.top + 1]
        else: pass

    def peek(self):
        if not self.is_empty():
            return self.array[self.top]
        else: pass



