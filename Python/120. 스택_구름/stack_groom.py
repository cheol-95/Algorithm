# stack = []
# input_size = int(input())
#
# for i in range(input_size):
#   command=int(input())
#   if command == 1:
#     try:
#       stack.pop()
#     except:
#       print('underflow')
#   elif command == 0:
#     tmp = input()
#     if len(stack) == 10:
#       print('overflow')
#     else:
#       stack.append(tmp)
#   else:
#     break
#
# for i in stack:
#   print(i, end=' ')


N = int(input())
stack = []

for _ in range(N):
  control = int(input())

  if control == 0: # 푸시
    if len(stack) == 10:
      print('overflow')
      continue
    stack.append(input())

  elif control == 1: # 팝
    if len(stack) == 0:
      print('underflow')
      continue
    stack.pop()

  else: # 종료
    break

for i in stack:
  print(i, end=' ')

