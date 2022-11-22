n = int(input())
arr = list(map(int, input().split()))
ans = 0
for i in range(n):
    k = arr[i]
    if k in arr[i+1:]:
        ans += 1

print(ans)