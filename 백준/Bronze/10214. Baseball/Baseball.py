t = int(input())

for _ in range(t):
    arr = [0, 0]

    for _ in range(9):
        a, b = map(int, input().split())
        arr[0] += a
        arr[1] += b

    if arr[0] > arr[1]:
        print("Yonsei")
    elif arr[0] < arr[1]:
        print("Korea")
    else:
        print("Draw")