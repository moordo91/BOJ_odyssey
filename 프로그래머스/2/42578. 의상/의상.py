from collections import defaultdict
def solution(clothes):
    answer = 1
    d = defaultdict(int)
    for n, t in clothes:
        d[t] += 1
    for k, v in d.items():
        answer *= (v + 1)
    return answer - 1