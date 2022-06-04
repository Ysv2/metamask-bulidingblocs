hexa = '89225c73a372572ce4742f09575389b42086b68e'
con = 16
alpha = 'abcdef'
num = [10,11,12,13,14,15]
total = 0
b = 1
for x in range(len(hexa)):
    if hexa[x] in alpha:
        a = alpha.find(hexa[x])
        mul = num[a]
        #total += num[a]*(con**(len(hexa)-b))
    else:
        mul = int(hexa[x])
    total += mul*(con**(len(hexa)-b))
    b+=1
print(total)
