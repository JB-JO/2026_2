def heappush(heap, n):
    heap.append(n)
    i = len(heap)-1
    while i != 1:
        pi = i // 2
        if n <= heap[pi]:
            break
        heap[i] = heap[pi]
        i = pi
    heap[i] = n

def heappop(heap): # 삭제 과정은 결국 빈칸 heap[pi]가 옮겨다니는 모양새
    size = len(heap) - 1
    if size == 0:
        return None
    pi = 1                                     # 부모 노드의 인덱스
    i = 2                                      # 자식 노드의 인덱스
    root = heap[1]                             # 삭제할 루트 노드
    last = heap[size]                          # 마지막 노드

    while i <= size:                           # 더 내려갈 자식이 있을 때까지 down-heap 과정 진행
        if i < size and heap[i] < heap[i + 1]: # 오른쪽 자식이 더 크면
            i += 1                             # 오른쪽 자식에 대해 처리
        if last >= heap[i]:                    # 자식이 더 작다면 종료
            break
        heap[pi] = heap[i]                     # 더 큰 자식을 부모위치로 # 이미 본래의 루트 노드 값은 root 변수에 저장
        pi = i                                 # 부모 위치가 자식 위치 i로 내려감
        i *= 2                                 # 자식은 일단 부모의 왼쪽 자식

    heap[pi] = last                            # 맨 마지막 노드를 부모 위치에 복사 # 부모 위치라고 하지만 결국은 그냥 빈칸에 때려박는 것,
    heap.pop()                                 # 맨 마지막 노드 삭제
    return root                                # 저장해 두었던 루트를 반환함.