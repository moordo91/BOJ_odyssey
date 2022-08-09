n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
arr =set(arr)
result = []
ans = []

def sol():
    if len(result) == m:
        print(' '.join(map(str, result)))
        return

    for i in arr:
        result.append(i)
        sol()
        result.pop()

sol()

    