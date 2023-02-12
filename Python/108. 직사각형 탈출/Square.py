x,y,w,h = map(int, input().split())
small = w-x if w-x < h-y else h-y
tmp = x if x < y else y
print(small) if small < tmp else print(tmp)