def prize1(x):
    if x == 0 or x > 21:
        return 0
    elif x == 1:
        return 5000000
    elif x <= 3:
        return 3000000
    elif x <= 6:
        return 2000000
    elif x <= 10:
        return 500000
    elif x <= 15:
        return 300000
    else:
        return 100000

def prize2(x):
    if x == 0 or x > 31:
        return 0
    elif x == 1:
        return 5120000
    elif x <= 3:
        return 2560000
    elif x <= 7:
        return 1280000
    elif x <= 15:
        return 640000
    else:
        return 320000

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    print(prize1(a) + prize2(b))