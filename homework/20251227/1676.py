a = int(input(""))
a1 = 1
a2 = 0

for i in range(1,a+1):
    a1 = a1*i

a1 = str(a1)

for i in reversed(a1):
    if int(i) == 0:
        a2 += 1
    else:
        break
    
print(a2)