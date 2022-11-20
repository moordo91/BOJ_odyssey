arr = []
for _ in range(10):
    arr.append(int(input()))

ass = [0 for _ in range(max(arr)+1)]
for item in arr:
    ass[item] += 1

print(sum(arr)//10)
print(ass.index(max(ass)))