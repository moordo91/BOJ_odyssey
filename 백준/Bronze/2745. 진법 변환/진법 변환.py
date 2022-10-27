a, b = input().split()

a = list(a)
b = int(b)
n = len(a)
ans = 0

for item in range(n):
    if 65 <= ord(a[item]) < 91:
        ans += (ord(a[item])-55)*b**(n-item-1)
    else:
        ans += int(a[item])*b**(n-item-1)

print(ans)