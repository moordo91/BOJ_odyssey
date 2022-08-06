a, b, c = map(int, input().split())

def sol(a, b, c):
    if b == 1:
        return a % c
    else:
        tmp = sol(a, b//2, c)
        if b % 2 == 0:
            return (tmp * tmp) % c
        else:
            return (tmp * tmp * a) % c

print(sol(a, b, c))