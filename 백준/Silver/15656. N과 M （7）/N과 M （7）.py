n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
result = []

def sol():
    if len(result) == m:
        print(' '.join(map(str, result)))
        return

    for i in range(n):
        # if arr[i] not in result:
        result.append(arr[i])
        sol()
        result.pop()

sol()