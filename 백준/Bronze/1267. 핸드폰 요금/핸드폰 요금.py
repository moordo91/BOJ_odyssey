import math
t = int(input())
k = list(map(int, input().split()))
y, m = 0, 0

for i in k:
    y += math.ceil((i+0.5) / 30) * 10
    m += math.ceil((i+0.5) / 60) * 15

if y > m:
    print('M', m)
elif y < m:
    print('Y', y)
else:
    print('Y M', y)