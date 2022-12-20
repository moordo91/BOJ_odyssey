def fibonacci(n):
    f = [0, 1, 1] + [i for i in range(n-2)]
    for i in range(3, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]

n = int(input())

print(fibonacci(n), n-2)
