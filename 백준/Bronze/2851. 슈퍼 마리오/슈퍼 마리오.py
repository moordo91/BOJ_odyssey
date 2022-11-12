arr = []

for _ in range(10):
    arr.append(int(input()))

tmp = float('inf')
idx = 0
for i in range(10):
    if abs(sum(arr[:i+1])-100) <= tmp:
        idx = i
        tmp = abs(sum(arr[:i+1])-100)

print(sum(arr[:idx+1]))
    