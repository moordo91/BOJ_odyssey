import math
from collections import defaultdict

def solution(progresses, speeds):
    days_left = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)]
    
    count = [1]
    max_day = days_left[0]
    day_dict = defaultdict(int)
    for i in range(1, len(days_left)):
        if max_day >= days_left[i]:
            count.append(count[-1])
        else:
            max_day = days_left[i]
            count.append(count[-1]+1)
    for c in count:
        day_dict[c] += 1
    return [v for _, v in day_dict.items()]