table =[('A', '.-'),    ('B', '-...'),  ('C', '-.-.'),  ('D', '-..'),
        ('E', '.'),     ('F', '..-.'),  ('G', '--.'),   ('H', '....'),
        ('I', '..'),    ('J', '.---'),  ('K', '-.-'),   ('L', '.-..'),
        ('M', '--'),    ('N', '-.'),    ('O', '---'),   ('P', '.--.'),
        ('Q', '--.-'),  ('R', '.-.'),   ('S', '...'),   ('T', '-'),
        ('U', '..-'),   ('V', '...-'),  ('W', '.--'),   ('X', '-..-'),
        ('Y', '-.--'),  ('Z', '--..') ]

def encode(ch):
    idx = ord(ch)-ord('A')
    return table[idx][1]

def decode_slow(code):
    for e in table:
        if code == e[1]:
            return e[0]
    return None


from BinaryTree import *

def make_morse_tree():
    root = TNode(None,None, None)
    for i in table:
        code = i[1]          # 모스 코드
        node = root
        for j in code:       # 모스 코드 각 부호에 대하여
            if j == '.':     # 점이라면 왼쪽으로 진행하고 왼쪽 노드가 비었으면 새로운 노드를 만들고 있으면 그쪽으로 이동
                if node.left is None:
                    node.left = TNode(None,None,None)
                node = node.left
            elif j == '-':   # 선이면 오른쪽으로 진행 왼쪽과 같음.
                if node.right is None:
                    node.right = TNode(None,None,None)
                node = node.right

        node.data = i[0]      # 코드의 알파벳
    return root

def decode(root, code):
    node = root
    for i in code:
        if i == '.':
            node = node.left
        elif i == '-':
            node = node.right
    return node.data





if __name__ == "__main__":
    morseCodeTree = make_morse_tree()
    string = input("입력 문장 : ")
    mlist = []
    for ch in string:
        code = encode(ch)
        mlist.append(code)
    print("Morse Code: ", mlist)
    print("Decoding  : ", end='')
    for code in mlist:
        ch = decode(morseCodeTree, code)
        print(ch, end='')
    print()

    for code in mlist:
        ch = decode_slow(code)
        print(ch, end='')
    print()
