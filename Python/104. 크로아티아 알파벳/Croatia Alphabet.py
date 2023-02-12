string = input()
croatia = ['c=','c-','dz=','d-','lj','nj','s=','z=']
for char in croatia:
    string = string.replace(char, 'A')
print(len(string))