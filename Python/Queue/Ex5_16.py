from CircularDequeue import *
from StackClass import *

D = CircularDequeue()
S = Stack(10)

for i in range(1, 9):
    D.add_rear(i)

print(D)

while not D.is_empty():
    S.push(D.delete_front())

print(S)

while not S.is_empty():
    D.add_rear(S.pop())

print(D)