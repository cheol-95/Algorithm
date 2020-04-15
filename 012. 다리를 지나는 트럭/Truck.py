def solution(bridge_length, weight, truck_weights):
    answer = 0 # 총 소요시간
    on = [] # 다리에 올라와있는 트럭 큐
    for i in truck_weights: # 트럭 수 만큼 반복
        while True:
            if len(on) == bridge_length: # 다리에 트럭이 가득 올라와있다면
                on.pop() # 가장 먼저 올라온 트럭 pop
            if(sum(on) + i) <= weight: # 다리위의 트럭 총 무게 + 다음 트럭무게 <= 최대하중
                on.insert(0, i) # 다음 트럭 진입
                answer += 1 # 소요시간 + 1
                break
            else: # 하중 제한때문에 다음 트럭을 올릴수가 없다면
                on.insert(0, 0) # 모든 트럭 1만큼 전진
                answer += 1 # 소요시간 + 1
    answer = answer + bridge_length # 마지막 트럭의 이동시간을 고려하지 않았으므로 다리의 길이만큼 더해준다
    return answer


bridge_length, weight, truck_weights = 2,10,[7,4,5,6]
# bridge_length, weight, truck_weights = 100,100,[10]
# bridge_length, weight, truck_weights = 100,100,[10,10,10,10,10,10,10,10,10,10]
print(solution(bridge_length, weight, truck_weights))