import copy

def dfs(graph, start, visited):
    visited[start] = True
    for nxt in graph[start]:
        if not visited[nxt]:
            dfs(graph, nxt, visited)
    return visited

def solution(n, wires):
    answer = float('inf')
    num_wires = len(wires)
    for i in range(num_wires):
        graph = [[] for _ in range(n)]
        wires_ = copy.deepcopy(wires)
        del wires_[i]
        for a, b in wires_:
            graph[a-1].append(b-1)
            graph[b-1].append(a-1)
        visited = [False] * n
        visited = dfs(graph, 1, visited)
        a = sum(v == True for v in visited)
        b = n - a
        answer = min(answer, abs(a - b))
    
    return answer