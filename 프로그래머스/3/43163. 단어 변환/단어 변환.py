import sys
from collections import deque
from itertools import combinations

def connect(word1, word2):
    return sum(c1 != c2 for c1, c2 in zip(word1, word2)) == 1

def bfs(graph, N, target, words):
    dist = {words[0]: 0}
    q = deque([0])
    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if words[nxt] not in dist:
                dist[words[nxt]] = dist[words[cur]] + 1
                q.append(nxt)
            if words[nxt] == target:
                return dist[words[nxt]]
    return 0
        

def solution(begin, target, words):
    words = [begin, *words]
    N = len(words)

    graph = [[] for _ in range(N)]
    for n1, n2 in combinations(range(N), 2):
        if connect(words[n1], words[n2]):
            graph[n1].append(n2)
            graph[n2].append(n1)

    answer = bfs(graph, N, target, words)
    return answer
