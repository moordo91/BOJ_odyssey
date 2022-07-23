n = int(input())
l = [0]

for i in range(1, n+1):
    j = 1
    min_l = float('inf')

    while j**2 <= i:
        min_l = min(min_l, l[i - j**2])
        j += 1
    
    l.append(min_l + 1)

print(l[n])