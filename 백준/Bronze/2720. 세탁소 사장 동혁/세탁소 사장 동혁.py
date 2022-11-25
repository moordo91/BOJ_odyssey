def sol(c):
    arr = [0, 0, 0, 0]
    coin = [25, 10, 5, 1]
    for i in range(4):
        arr[i] = c // coin[i]
        c = c % coin[i]
    return arr

t = int(input())

for i in range(t):
    c = int(input())
    for j in range(4):
        print(sol(c)[j], end=' ')
    print()
