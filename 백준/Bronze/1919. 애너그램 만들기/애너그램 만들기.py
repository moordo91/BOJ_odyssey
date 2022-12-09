a = list(input())
b = list(input())
k = 0

a.sort()
b.sort()

c = list(set(a) & set(b))
d = list((set(a) | set(b)) - (set(a) & set(b)))

for i in c:
    if abs(a.count(i) - b.count(i)) > 0:
        k += abs(a.count(i) - b.count(i))
    else:
        continue
for i in d:
    k += a.count(i)
    k += b.count(i)
    
print(k)