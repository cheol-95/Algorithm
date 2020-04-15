N = int(input())
heap = []
for i in range(N):
    num = int(input())
    if num:
        heap.append(num)  # heap에 추가
    else:
        if not heap: # 0입력, heap 비어있음
            print('0')
            continue
        tmp = list(map(abs,heap)) # 절댓값 리스트 생성
        tMin = min(tmp) # 절댓값 가장 낮은 수
        tIndex = tmp.index(tMin) # 해당 인덱스
        print(heap[tIndex]) # 해당 수 출력
        del heap[tIndex] # 해당 수 삭제

'''
# heapq + try ~ except 사용 
import heapq
N = int(input())
heap = []
for i in range(N):
    num = int(input())
    if num:
        heapq.heappush(heap, (abs(num), num))  # 튜플로 삽입(절댓값, 실제값), 여기서 절대값이 우선순위가 된다
    else:
        try:
            print(heapq.heappop(heap)[1]) # 우선순위로 판단해 삭제하고, 실제값 출력
        except:
            print('0')
'''