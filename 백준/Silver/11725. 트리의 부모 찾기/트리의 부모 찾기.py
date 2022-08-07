import sys; gets = sys.stdin.readline
sys.setrecursionlimit(10**6)

def DFS(start, tree, parents):
    for i in tree[start]:
        if parents[i] == 0:
            parents[i] = start
            DFS(i, tree, parents)

n = int(gets())

tree = [[] for _ in range(n+1)]
parents = [0 for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, gets().split())
    tree[a].append(b)
    tree[b].append(a)

DFS(1, tree, parents)

for i in range(2, n+1):
    print(parents[i])