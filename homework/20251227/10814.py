a = int(input())
wjdfuf = []

for i in range(a):
    age,name = input().split()
    wjdfuf.append((int(age),name))
    
wjdfuf.sort(key=lambda x : x[0])

print()

for age,name in wjdfuf:
    print(age,name)