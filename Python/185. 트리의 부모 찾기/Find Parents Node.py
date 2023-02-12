import collections
import sys
input = sys.stdin.readline

N = int(input())

parent = [0] * (N + 1)
parent[1] = 1
tree = collections.defaultdict(list)

for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

stack = [1]
while stack:
    node = stack.pop()
    for child in tree[node]:
        if not parent[child]:
            parent[child] = node
            stack.append(child)

for i in parent[2:]:
    print(i)