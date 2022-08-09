n, m = map(int, input().split())
result = [0]

def sol():
    if len(result) > m:
        print(' '.join(map(str, result[1:])))
        return

    for i in range(1, n+1):
        if i >= result[-1]:
            result.append(i)
            sol()
            result.pop()

sol()