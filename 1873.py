n = int(input())

arr = [
  "tesourapapel",
  "papelpedra",
  "pedralagarto",
  "lagartospock",
  "spocktesoura",
  "tesouralagarto",
  "lagartopapel",
  "papelspock",
  "spockpedra",
  "pedratesoura"
  ]

for i in range(n):
  string = str(input())
  values = string.split(' ')
  a = values[0]
  b = values[1]
  if a == b:
    print("empate")
  elif a + b in arr:
    print("rajesh")
  else:
    print("sheldon")
