def sol(arr, a, b):
    temp = reversed(arr[a:b+1])
    arr[a:b+1] = temp
    return arr

arr = [i for i in range(21)]
for _ in range(10):
    a, b = map(int, input().split())
    arr = sol(arr, a, b)

del arr[0]
for i in arr:
    print(i, end=' ')