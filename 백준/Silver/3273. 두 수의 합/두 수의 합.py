import sys; gets = sys.stdin.readline

n = int(gets())
arr = list(map(int, gets().split()))
x = int(gets())
cnt = 0

arr.sort()

for i in arr:
    if i > x/2:
        break
    if x-i in arr and x-i != i:
        cnt += 1
print(cnt)