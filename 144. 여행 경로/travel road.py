# import collections
# def solution(tickets):
#     routes = collections.defaultdict(list)
#     for start, destination in tickets:
#         routes[start].append(destination)
#
#     for route in routes:
#         routes[route].sort(reverse=True)
#
#     stack = ["ICN"]
#     path = []
#
#     while stack:
#         top = stack[-1]
#
#         if top not in routes or len(routes[top]) == 0:
#             path.append(stack.pop())
#         else:
#             stack.append(routes[top].pop())
#
#     return path[::-1]

import collections
def solution(tickets):
    ticket = collections.defaultdict(list)
    for a, b in tickets:
        ticket[a].append(b)
        ticket[a].sort(reverse=True)

    stack = ["ICN"]
    result = []
    while stack:
        start = stack[-1]

        if start not in ticket or len(ticket[start]) == 0:
            result.append(stack.pop())
        else:
            stack.append(ticket[start].pop())

    return result[::-1]


# tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
print(solution(tickets))
