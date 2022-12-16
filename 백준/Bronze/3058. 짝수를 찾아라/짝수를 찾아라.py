def sol(arr):
    ans = []
    for i in arr:
        if i % 2 == 0:
            ans.append(i) 
    return ans

t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))
    ans = sol(arr)
    print(sum(ans), min(ans))