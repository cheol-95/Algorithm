def solution(bridge_length, weight, truck_weights):
    answer = 0
    on = []
    for i in truck_weights:
        while True:
            if len(on) == bridge_length:
                on.pop()
            if(sum(on) + i) <= weight:
                on.insert(0, i)
                answer += 1
                break
            else:
                on.insert(0, 0)
                answer += 1
    answer = answer + bridge_length
    return answer


bridge_length, weight, truck_weights = 2,10,[7,4,5,6]
# bridge_length, weight, truck_weights = 100,100,[10]
# bridge_length, weight, truck_weights = 100,100,[10,10,10,10,10,10,10,10,10,10]
print(solution(bridge_length, weight, truck_weights))