arr = [[0 for _ in range(100)] for _ in range(100)]
count = 0
num = int(input())
for i in range(num):
    x,y = map(int,input().split())
    for a in range(10):
        for b in range(10):
            arr[x+b][y+a] = 1
        
for i in arr:
    for j in i:
        if j == 1:
            count += 1
        
print(count)