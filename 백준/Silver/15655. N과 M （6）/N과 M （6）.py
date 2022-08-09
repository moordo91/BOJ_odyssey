n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
result = []

def sol(start):
    if len(result) == m:
        print(' '.join(map(str, result)))
        return

    for i in range(start, n):
        if arr[i] not in result:
            result.append(arr[i])
            sol(i+1)
            result.pop()

sol(0)