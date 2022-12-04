def sol(n, arr):
    arr = list(arr)
    del arr[n-1]
    for i in arr:
        print(i, end='')
    print()
    
t = int(input())

for _ in range(t):
    n, arr = map(str, input().split())
    sol(int(n), arr)
