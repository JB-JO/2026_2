def hash_fn(key, m):
    sum = 0
    for c in key:
        sum += ord(c)
    return sum % m