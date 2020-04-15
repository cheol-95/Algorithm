N = int(input())
heap = []
for i in range(N):
    num = int(input())
    if num == 0:
        if not heap: # 0입력, heap 비어있음
            print('0')
            continue
        tmp = list(map(abs,heap))
        tMin = min(tmp) # 절댓값 가장 낮은 수
        tIndex = tmp.index(tMin) # 해당 인덱스
        print(heap[tIndex]) # 해당 수 출력
        del heap[tIndex] # 해당 수 삭제
    else:
        heap.append(num) # heap에 추가