t = int(input())
for _ in range(t):
    n = int(input())
    bn = bin(n)[::-1]

    for i in range(len(bn)):
        if bn[i] == '1':
            print(i, end=' ')
    print()