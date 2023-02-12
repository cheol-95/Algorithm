def solution(bridge_length, weight, truck_weights):
    cnt = 0
    on = 0
    on_bridge = [0 for i in range(bridge_length)]
    while truck_weights:
        cnt += 1
        on -= on_bridge.pop()
        if on + truck_weights[0] <= weight:
            tmp = truck_weights.pop(0)
            on_bridge.insert(0, tmp)
            on += tmp
        else:
            on_bridge.insert(0, 0)
    return cnt + bridge_length

'''
#이전 코드
def solution(bridge_length, weight, truck_weights):
    answer = 0 # 총 소요시간
    on = [] # 다리에 올라와있는 트럭 큐
    for i in truck_weights: # 트럭 수 만큼 반복
        while True:
            if len(on) == bridge_length: # 다리에 트럭이 가득 올라와있다면
                on.pop() # 가장 먼저 올라온 트럭 pop
                print('a', i, on)
            if(sum(on) + i) <= weight: # 다리위의 트럭 총 무게 + 다음 트럭무게 <= 최대하중
                on.insert(0, i) # 다음 트럭 진입
                answer += 1 # 소요시간 + 1
                print('b', i, on)
                break
            else: # 하중 제한때문에 다음 트럭을 올릴수가 없다면
                on.insert(0, 0) # 모든 트럭 1만큼 전진
                answer += 1 # 소요시간 + 1
                print('c', i, on)
    answer = answer + bridge_length # 마지막 트럭의 이동시간을 고려하지 않았으므로 다리의 길이만큼 더해준다
    return answer
'''