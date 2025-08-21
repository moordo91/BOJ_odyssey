from collections import deque

def solution(arr):
    q = deque(arr)
    curr = q.popleft()
    answer = [curr]
    while q:
        curr = q.popleft()
        if answer[-1] != curr:
            answer.append(curr)
    return answer