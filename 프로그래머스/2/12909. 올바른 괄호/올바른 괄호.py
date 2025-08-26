def solution(s):
    answer = True
    
    list_s = list(s)
    cnt = 0
    first = True
    for e in list_s:
        if e == '(':
            cnt += 1
        else:
            cnt -= 1
        if first and cnt < 0:
            first = False
            return False
        
    if cnt != 0:
        return False

    return True