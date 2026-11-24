def sequential_search(a, key, low, high) :
    for i in range(low, high + 1) :
        if a[i] == key:
            return i
    return -1

def binary_search(a, key, low, high) :
    if low > high :
        return -1

    mid = (low + high) // 2

    if a[mid] == key:
        return mid
    elif a[mid] > key:
        return binary_search(a, key, low, mid - 1)
    else:
        return binary_search(a, key, mid + 1, high)

def binary_search_iter(a, key, low, high) :
    while low <= high:
        mid = (low + high) // 2

        if a[mid] == key:
            return mid
        elif a[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
    return -1