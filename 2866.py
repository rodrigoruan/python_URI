n = int(input())

for i in range(n):
  string = str(input())
  lowerStr = ""
  for letter in string:
    if letter.islower():
      lowerStr += letter
  print(lowerStr[::-1])