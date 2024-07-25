import sys
input = sys.stdin.readline

def check_list(b):
    cnt = 0
    for i in b:
        if i > 0:
            cnt += 1
    if cnt <= 2:
        return True
    else:
        return False

n = int(input())
a = list(map(int, input().split()))
l = 0
r = 0
max_n = 0
basket = [0] * 10
basket[a[0]] += 1

while True:
    if check_list(basket):
        max_n = max(max_n, r-l+1)
        r += 1
        if r == n:
            break
        basket[a[r]] += 1
    else:
        basket[a[l]] -= 1
        l += 1

print(max_n)