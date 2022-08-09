n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
result = [0]

def sol():
    if len(result[1:]) == m:
        print(' '.join(map(str, result[1:])))
        return

    for i in range(n):
        # if arr[i] not in result:
        if arr[i] >= result[-1]:
            result.append(arr[i])
            sol()
            result.pop()

sol()