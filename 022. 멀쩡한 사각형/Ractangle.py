from math import gcd
def solution(w,h):
    tmp = gcd(w,h)
    if w > h: # h를 큰 수로 변경
        w,h = h,w

    ww = w//tmp
    hh = h//tmp
    a=hh/2
    if str(type(a)) == "<class 'float'>":
        a = int(a)+1

    answer = w*h-(a*ww*tmp)
    if answer == 1:
        return 0
    return w*h-(a*ww*tmp)

w, h = 8,12
print(solution(w, h))