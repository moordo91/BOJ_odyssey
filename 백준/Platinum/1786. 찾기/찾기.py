import sys
input = sys.stdin.readline

t = list(input())[:-1]
p = list(input())[:-1]

def get_pi(p):
    pi = [0] * len(p)
    p = list(p)
    j = 0
    for i in range(1, len(p)):
        while j > 0 and p[i] != p[j]:
            j = pi[j-1]
        if p[i] == p[j]:
            j += 1
            pi[i] = j
    return pi

def kmp(t, p):
    pi = get_pi(p)
    j = 0
    cnt = 0
    idx = []
    for i in range(len(t)):
        while j > 0 and t[i] != p[j]:
            j = pi[j-1]
        if t[i] == p[j]:
            if j == len(p)-1:
                idx.append(i-len(p)+2)
                cnt += 1
                j = pi[j]
            else:
                j += 1
    return cnt, idx

cnt, idx = kmp(t, p)

print(cnt)
for i in idx:
    print(i, end=' ')