from collections import defaultdict

def solution(participant, completion):
    answer = ''
    p = defaultdict(int)
    for name in participant:
        p[name] += 1
    for name in completion:
        p[name] -= 1
    for k, v in p.items():
        if v > 0:
            answer = k
            break
    return answer