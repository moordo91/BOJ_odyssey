n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr = set(arr)
arr = sorted(list(arr))
result = [0]
ans = []

def sol():
    if len(result) > m:
        print(' '.join(map(str, result[1:])))
        return

    for i in arr:
        if i >= result[-1]:
            result.append(i)
            sol()
            result.pop()

sol()

    