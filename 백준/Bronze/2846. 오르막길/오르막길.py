n = int(input())
arr = list(map(int, input().split()))
d = []
ans = [0 for _ in range(n)]

for i in range(n-1):
    d.append(arr[i+1]-arr[i])

j = 0
for i in range(n-1):
    if d[i] > 0:
        ans[j] += d[i]
    else:
        j += 1

print(max(ans))