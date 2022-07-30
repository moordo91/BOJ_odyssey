global ans
ans = 0
n = int(input())
board = [[False for _ in range(n)] for _ in range(n)]
check1 = [False for _ in range(n)]
check2 = [False for _ in range(2*n-1)]  # 우상향 대각선: x+y
check3 = [False for _ in range(2*n-1)]  # 우하향 대각선: x-y+n-1

def sol(cnt):
    global ans
    if cnt >= n:
        ans += 1
        return
    for i in range(n):
        if not (board[cnt][i] or check1[i] or check2[cnt+i] or check3[i-cnt+n-1]):
            board[cnt][i] = True
            check1[i], check2[cnt+i], check3[i-cnt+n-1] = True, True, True
            sol(cnt+1)
            board[cnt][i] = False
            check1[i], check2[cnt+i], check3[i-cnt+n-1] = False, False, False

sol(0)
print(ans)