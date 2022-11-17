a, b = 100, 100

t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    if x > y:
        b -= x
    elif x < y:
        a -= y
    else:
        continue

print(a)
print(b)