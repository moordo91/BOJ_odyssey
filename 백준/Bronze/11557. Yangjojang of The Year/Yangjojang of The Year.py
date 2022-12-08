def sol(n):
    dic = {}
    for _ in range(n):
        a, b = map(str, input().split())
        dic[a] = int(b)

    print(max(dic, key=dic.get))

t = int(input())
for _ in range(t):
    n = int(input())
    sol(n)