import collections
def get_next(name, ns, idx):
    q = collections.deque([[idx, 0]]) # 현재 idx, 변화에 필요한 cnt
    while q:
        i, cnt = q.popleft()
        if name[i] != ns[i]:
            return i, cnt
        q.append([(idx + 1) % len(name), cnt + 1])
        q.append([(idx - 1) % len(name), cnt + 1])

def solution(name):
    cnt = 0
    idx = 0
    ns = 'A'*len(name)
    while name != ns:
        idx, t_cnt = get_next(name, ns, idx)
        cnt += t_cnt

        ord_name, ord_ns = ord(name[idx]), ord(ns[idx])
        direct = abs(ord_name - ord_ns)
        rotate = (ord('Z') - max(ord_name, ord_ns)) + (min(ord_name, ord_ns) - ord('A')) + 1

        cnt += min(direct, rotate)
        ns = ns[:idx] + name[idx] + ns[idx+1:]
        if name == ns:
            return cnt

name = 'JEROEN'
print(solution(name))


'haaq'