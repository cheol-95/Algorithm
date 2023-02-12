N = int(input())

def compare(people_list, people):
  count = 1
  for other in people_list:
    if other[0] > people[0] and other[1] > people[1]:
      count += 1
  return str(count)

people_list = [list(map(int, input().split())) for _ in range(N)]

data = list(map(lambda people: compare(people_list, people), people_list))
print(' '.join(data))