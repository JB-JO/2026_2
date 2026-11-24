from CircularQueue import *
from CircularDequeue import *

D = CircularDequeue()
Q = CircularQueue()

for i in range (1, 9): #1~8까지 D라는 덱에 추가
    D.add_rear(i)

print(D)

while not D.is_empty(): # Q라는 queue에 D에 있는 값을 뒤에서부터 빼서 삽입함.
    Q.enqueue(D.delete_rear())

print(Q)

while not Q.is_empty(): # Q에 들어가 있는 순서대로 다시 D에 추가해줌.
    D.add_rear(Q.dequeue())

print(D)




