n=int(input())

for i in range(n):
  alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" * 2
  string = str(input())
  num = int(input())
  newStr = ""
  for i in string:
    newStr += alp[alp.index(i) - num]
  print(newStr)
