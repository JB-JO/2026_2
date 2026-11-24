M = int(input())

table = [None]*M

def hash_fn(key):
    return key % M

def insert(key):
    i = hash_fn(key)
    count = M
    while count > 0:
        if table[i] is None or table[i] == -1:
            break
        i = (i + 1) % M
        count -= 1

    if count > 0:
        table[i] = key

def search(key):
    i = hash_fn(key)
    count = M
    while count > 0:
        if table[i] is None:
            return None
        if table[i] == key:
            return i
        i = (i + 1) % M
        count -= 1

    return None

def delete(key):
    i = hash_fn(key)
    count = M
    while count > 0:
        if table[i] == key:
            table[i] = -1
            return
        if table[i] is None:
            return
        i = (i + 1) % M
        count -= 1
