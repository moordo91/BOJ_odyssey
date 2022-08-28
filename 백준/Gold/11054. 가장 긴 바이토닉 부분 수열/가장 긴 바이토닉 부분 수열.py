n = int(input())
arr = list(map(int, input().split()))
rev_arr = arr[::-1]

dpU = [1 for _ in range(n)]
dpD = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dpU[i] = max(dpU[i], dpU[j]+1)
        if rev_arr[i] > rev_arr[j]:
            dpD[i] = max(dpD[i], dpD[j]+1)

ans = [0 for _ in range(n)]
for i in range(n):
    ans[i] = dpU[i] + dpD[n-i-1] - 1

print(max(ans))