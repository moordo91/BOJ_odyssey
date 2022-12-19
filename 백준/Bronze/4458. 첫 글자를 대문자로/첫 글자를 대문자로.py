def sol(x):
    x = list(x)
    if ord(x[0]) >= 97:
        x[0] = chr(ord(x[0]) - 32)
    x = ''.join(i for i in x)
    return x

t = int(input())
for _ in range(t):
    print(sol(input()))