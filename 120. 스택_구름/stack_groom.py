stack = []
input_size = int(input())

for i in range(input_size):
  command=int(input())
  if command == 1:
    try:
      stack.pop()
    except:
      print('underflow')
  elif command == 0:
    tmp = input()
    if len(stack) == 10:
      print('overflow')
    else:
      stack.append(tmp)
  else:
    break

for i in stack:
  print(i, end=' ')