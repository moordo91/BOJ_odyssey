from collections import deque
import copy

def solution(progresses, speeds):
    answer = []
    chk = [False] * len(progresses)
    while sum(answer) < len(progresses):
        for i, (p, s) in enumerate(zip(progresses, speeds)):
            progresses[i] = p + s
        cnt = 0
        for p in progresses:
            if p >= 100:
                cnt += 1
            else:
                break
        
        if cnt > sum(chk):
            answer.append(cnt - sum(chk))
        for i in range(cnt):
            chk[i] = True
    return answer