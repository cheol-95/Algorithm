import collections
def solution(tickets):
    routes = collections.defaultdict(list)
    for start, destination in tickets:
        routes[start].append(destination)

    for route in routes:
        routes[route].sort(reverse=True)

    stack = ["ICN"]
    path = []

    while stack:
        top = stack[-1]

        if top not in routes or len(routes[top]) == 0:
            path.append(stack.pop())
        else:
            stack.append(routes[top].pop())

    return path[::-1]

tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
print(solution(tickets))
