n, m = map(int, input().split())
arr = []

def sol(start):
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return
    for i in range(start, n+1):
        if i not in arr:
            arr.append(i)
            sol(i+1)
            arr.pop()

sol(1)