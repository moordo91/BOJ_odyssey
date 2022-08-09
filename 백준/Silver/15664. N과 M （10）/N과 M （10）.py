n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
visited = [False for _ in range(n)]
result = []
ans = []

def sol(start):
    if len(result) == m:
        result_str = ' '.join(map(str, result))
        if result_str not in ans:
            ans.append(result_str)
            print(result_str)
            return

    for i in range(start, n):
        if not visited[i]:
            result.append(arr[i])
            visited[i] = True
            sol(i+1)
            result.pop()
            visited[i] = False

sol(0)

    