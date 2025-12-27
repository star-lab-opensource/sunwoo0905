z = 0
n = int(input())
for i in range(n):
    story = int(input())
    room = int(input())
    arr = [[0 for _ in range(room)] for _ in range(story+1)]
    for x in range(room):
        arr[0][x] = x + 1
    for s in range(1,story+1):
        for l in range(room):
            if l == 0:
                arr[s][l] = arr[s-1][l]
            else:
                arr[s][l] = arr[s][l-1] + arr[s-1][l]
    print(arr[story][room-1])