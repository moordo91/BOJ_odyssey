import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input()
target = 'I' + 'OI'*n

def get_pi(target):
    pi = [0] * len(target)
    target = list(target)
    j = 0
    for i in range(1, len(target)):
        while j > 0 and target[i] != target[j]:
            j = pi[j-1]
        if target[i] == target[j]:
            j += 1
            pi[i] = j
    return pi

def kmp(s, target):
    pi = get_pi(target)
    j = 0
    cnt = 0
    for i in range(len(s)):
        while j > 0 and s[i] != target[j]:
            j = pi[j-1]
        if s[i] == target[j]:
            if j == len(target)-1:
                cnt += 1
                j = pi[j]
            else:
                j += 1
    return cnt

print(kmp(s, target))
