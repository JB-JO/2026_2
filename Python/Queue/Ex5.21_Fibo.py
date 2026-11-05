from CircularQueue import *

def fibonacci(n):
    F = CircularQueue()
    F.enqueue(0)
    F.enqueue(1)
    if n < 0:
        return None
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for i in range(2, n + 1):
            f0 = F.dequeue()
            f1 = F.peek()
            F.enqueue(f0 + f1)

        F.dequeue()
        return F.dequeue()




S = fibonacci(100)
print(S)