n = int(input())

for i in range(n):
    strg = str(input())
    highest = 0
    obj = {}
    for i in strg:
        i = i.lower()
        if i.isalpha():
            if i in obj:
                obj[i] += 1
            else:
                obj[i] = 1
            if obj[i] > highest:
                highest = obj[i]
    newStr = ""
    for i in obj:
        if obj[i] == highest:
            newStr += i
    print(''.join(sorted(newStr)))