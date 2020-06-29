def solution(routes):
    answer = 0
    routes.sort()
    standard = routes[0][1]
    routes.pop(0)
    answer+=1

    for route in routes:
        if route[0] <= standard:
            standard = min(route[1],standard)
        else:
            standard = route[1]
            answer+=1
    return answer

routes = [[-20, 15], [-14, -5], [-18, -13], [-5, -3]]
print(solution(routes))