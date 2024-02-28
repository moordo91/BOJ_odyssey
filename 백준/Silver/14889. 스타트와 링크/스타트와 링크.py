import sys
input = sys.stdin.readline

n = int(input())
visited = [False for _ in range(n)]
mat = [list(map(int, input().split())) for _ in range(n)]
dif = 1e9

def dfs(idx, chosen_players):
    global dif
    if chosen_players == n // 2:
        start = 0
        link = 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    start += mat[i][j]
                elif not visited[i] and not visited[j]:
                    link += mat[i][j]
        dif = min(dif, abs(start - link))
        return
    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(i+1, chosen_players+1)
            visited[i] = False
            
dfs(0, 0)
print(dif)