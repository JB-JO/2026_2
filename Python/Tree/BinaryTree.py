class TNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


def preorder(n):
    if n is not None:
        print(n.data, end=' ')
        preorder(n.left)
        preorder(n.right)

def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.data, end=' ')
        inorder(n.right)

def postorder(n):
    if n is not None:
        postorder(n.left)
        postorder(n.right)
        print(n.data, end=' ')


from CircularQueue import *

def levelorder(root):
    queue = CircularQueue()
    queue.enqueue(root)
    while not queue.is_empty():
        n = queue.dequeue()
        if n is not None:
            print(n.data, end=' ')
            queue.enqueue(n.left)
            queue.enqueue(n.right)

def count_node(n):
    if n is None:
        return 0
    else:
        return 1 + count_node(n.left) + count_node(n.right)

def count_leaf(n):
    if n is None:                            # 공백 트리
        return 0
    elif n.left is None and n.right is None: # 단말 노드 --> 1을 반환
        return 1
    else:                                    # 비단말 노드 --> 좌우 서브트리의 결과 합을 반환
        return 1 + count_leaf(n.left) + count_leaf(n.right)

def calc_height(n):
    if n is None:
        return 0
    h_left = calc_height(n.left)
    h_right = calc_height(n.right)
    if h_left > h_right:
        return h_left + 1
    else:
        return h_right + 1