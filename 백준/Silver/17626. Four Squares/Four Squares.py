n = int(input())
l = [0]
for i in range(1, n+1):
    m = float('inf')
    j = 1
    while j**2 <= i:
        m = min(m, l[i - j**2])
        j += 1
    l.append(m+1)

print(l[n])