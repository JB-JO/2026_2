class Node:
    def __init__(self, elem,link=None):
        self.elem = elem
        self.link = link

class LinkedStack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def is_full(self):
        return False

    def push(self,elem):
        self.top = Node(elem, self.top)  #요소 elem을 이용해 노드를 만들고, 링크를 상단 노드로 연결하면 top은 이 노드를 가리키게됨.

    def pop(self):
        if not self.is_empty(): #공백인지 검사
            n = self.top #공백이 아니라면 n이라는 변수에 현재 top이 가리키는 노드의 주소를 저장
            self.top = self.top.link #이 코드로 top은 현재 가리키는 노드의 다음 노드를 가리킴
            return n.data #원래의 top이 가리키던 노드가 가진 data를 출력함.
        else: #위의 조건을 불만족했다는 의미는 현재 스택이 비었다는 말이므로 아무것도 출력하지 않음.
            return None

    def peek(self):
        if not self.is_empty():
            return self.top.elem
        else:
            return None

    def size(self):
        node = self.top
        count = 0
        while not node is None:
            node = node.link
            count += 1
        return count

    def __str__(self):
        arr = [] #요소들을 저장할 공백의 리스트
        node = self.top
        while not node is None:
            arr.append(node.elem) #각 노드의 elem을 리스트에 추가시킴
            node = node.link #다음 노드로 이동함.
        return str(arr) #문자열로 변환하여 리스트 출력.
