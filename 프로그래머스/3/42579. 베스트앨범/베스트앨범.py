from collections import defaultdict, OrderedDict

def solution(genres, plays):
    g_dict = defaultdict(int)
    p_dict = {}
    for i, (g, p) in enumerate(zip(genres, plays)):
        g_dict[g] += p
        p_dict[i] = (p, g)
    
    g_dict = OrderedDict(sorted(g_dict.items(), key=lambda x: x[1], reverse=True))
    p_dict = OrderedDict(sorted(p_dict.items(), key=lambda x: x[1][0], reverse=True))
    
    answer = []
    for genre in g_dict.keys():
        cnt = 0
        for k, (p_n, g) in p_dict.items():
            if cnt >= 2:
                break
            if g == genre:
                cnt += 1
                answer.append(k)
    print(g_dict)
    print(p_dict)
    return answer