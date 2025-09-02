def dfs(graph, start, visited, prev):
    visited[start] = True
    for nxt in graph[start]:
        if nxt != prev and visited[nxt]:
            return True
        if not visited[nxt]:
            is_cycle = dfs(graph, nxt, visited, start)
            if is_cycle is True:
                return True
    return False

def solution(n, costs):
    costs = sorted(costs, key=lambda x: x[2])
    graph = [[] for _ in range(n)]
    answer = 0
    for (a, b, c) in costs:
        graph[a].append(b)
        graph[b].append(a)
        answer += c
        visited = [False] * n
        is_cycle = dfs(graph, a, visited, -1)
        if is_cycle is True:
            graph[a].pop()
            graph[b].pop()
            answer -= c
    return answer