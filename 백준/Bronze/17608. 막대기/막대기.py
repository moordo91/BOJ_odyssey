n = int(input())

arr = []
ans = []

for _ in range(n):
    arr.append(int(input()))

for i in range(n):
    if arr[i] > arr[-1]:
        while len(ans) > 0 and arr[i] >= ans[-1]:
            ans.pop()
        ans.append(arr[i])
ans.append(arr[-1])
print(len(ans))
