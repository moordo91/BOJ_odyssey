import sys; gets = sys.stdin.readline
n = int(gets())
m = int(gets())
s = gets().strip()

if 2*n+1 > m:
    print(0)
    exit(0)

i, stk, cnt = 0, 0, 0
while m - 2 >= i:
    if s[i:i+3] == "IOI":
        i += 2
        stk += 1
    else:
        if stk >= n:
            cnt += stk - n + 1
        stk = 0
        i += 1
print(cnt)