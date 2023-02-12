string = input()
center = len(string)/2
cnt = 0
 
while cnt < center:
	print(string[cnt],end='')
	cnt += 1
	if cnt > center:
		break
	print(string[-cnt],end='')