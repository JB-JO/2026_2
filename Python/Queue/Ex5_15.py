from CircularQueue import *
from CircularDequeue import *

D = CircularDequeue()
Q = CircularQueue()

for i in range (1, 9):
    D.add_rear(i)

print(D)

while not D.is_empty():
    Q.enqueue(D.delete_rear())

print(Q)

while not Q.is_empty():
    D.add_rear(Q.dequeue())

print(D)




