from collections import deque

def solution(priorities, location):
    answer = 1
    N = len(priorities)
    max_priority = max(priorities)
    proc_q = deque(priorities)
    loc_q = deque([i for i in range(N)])
    
    while proc_q:
        cur_p = proc_q.popleft()
        cur_l = loc_q.popleft()
        if cur_p < max_priority:
            proc_q.append(cur_p)
            loc_q.append(cur_l)    
        elif cur_p == max_priority:
            if cur_l == location:
                return answer
            elif max_priority not in proc_q:
                max_priority = max(proc_q)
            answer += 1