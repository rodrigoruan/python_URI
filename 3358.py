n = int(input())

def verify_word(string):
  vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
  c = 0
  for l in string:
    if l not in vowels:
      c += 1
    else:
      c = 0
    if c >= 3:
      return string + " nao eh facil"
  return string + " eh facil"

for i in range(n):
  string = str(input())
  print(verify_word(string))
