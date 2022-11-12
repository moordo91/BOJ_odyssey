arr = []
ans = [False for _ in range(1001)]

for i in range(1, 45):
    arr.append(i*(i+1)//2)


for i in arr:
    for j in arr:
        for k in arr:
            if i+j+k <= 1000:
                ans[i+j+k] = True

t = int(input())
for _ in range(t):
    k = int(input())
    if ans[k]:
        print(1)
    else:
        print(0)