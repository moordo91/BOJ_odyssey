def sol(k, d):
    if k > d:
        print("NE")
    else:
        print("DA")

n, w, h = map(int, input().split())
d = (w*w + h*h) ** 0.5

for _ in range(n):
    k = int(input())
    sol(k, d)