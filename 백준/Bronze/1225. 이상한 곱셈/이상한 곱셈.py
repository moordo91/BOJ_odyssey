def sol(a):
    arr = []
    for i in a:
        arr.append(int(i))
    return arr

a, b = map(str, input().split())

a = sol(a)
b = sol(b)
ans = 0

for i in a:
    for j in b:
        ans += i * j
        
print(ans)