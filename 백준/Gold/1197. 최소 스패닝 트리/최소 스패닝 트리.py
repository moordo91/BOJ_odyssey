import sys
input = sys.stdin.readline

def get_parent(parents, x):
    if parents[x] == x:
        return x
    parents[x] = get_parent(parents, parents[x])
    return parents[x]

def union_parents(parents, a, b):
    a = get_parent(parents, a)
    b = get_parent(parents, b)

    if a < b:
        parents[b] = a
    else:
        parents[a] = b

def same_parent(parents, a, b):
    return get_parent(parents, a) == get_parent(parents, b)

graph = []
v, e = map(int, input().split())
parents = [i for i in range(v+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph.append((c, a, b))

graph.sort()

answer = 0
for c, a, b in graph:
    if not same_parent(parents, a, b):
        union_parents(parents, a, b)
        answer += c
        
print(answer)