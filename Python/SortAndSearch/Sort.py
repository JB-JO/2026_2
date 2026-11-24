def selection_sort(a): # 0번 인덱스를 최초 위치로 잡고 하나씩 인덱스를 증가 시키며 가장 작은 수를 찾아 해당 인덱스와 교환.
    n = len(a)
    for i in range(n - 1):
        least = i
        for j in range(i + 1, n): # 최선의 입력과 최악의 입력 모두 외부루프로 자리를 정하고 내부루프로 비교하므로 O(n^2)
            if a[j] < a[least]:
                least = j
        a[i], a[least] = a[least], a[i]
        print_step(a, i + 1)

def print_step(arr, val):
    print("   Step % 2d = " % val, end="")
    print(arr)

def insertion_sort(a): # 자리 교환이 아닌 중간에 그냥 끼워넣는 형식
    n = len(a)
    for i in range(1, n): # 최선의 입력은 모두 정렬된 경우 내부루프를 사용하지 않으므로 O(n)
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]: #최악의 입력은 내부 루프를 항상 I번 반복하므로 O(n^2)
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
        print_step(a, i)

def bubble_sort(a):
    n = len(a)
    for i in range(n - 1, 0, -1): # 입력 요소의 수만큼 스캔수를 확정
        b_changed = False
        for j in range(i): # 인접한 요소의 비교 최선의 경우 스캔 한번이 O(n)
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                b_changed = True

        if not b_changed: break
        print_step(a, n - i)