stack = []
count = 0

input_size = int(input())

for i in range(input_size):
  command = int(input())
  if command == 1:
    try:
      stack.pop()
    except:
      print('underflow')
  elif command == 0:
    if len(stack) == 10:
      print('overflow')
    else:
      tmp = input()
      stack.append(tmp)
    print(int(tmp))
  else:
    break

if stack:
  print(' '.join(stack))