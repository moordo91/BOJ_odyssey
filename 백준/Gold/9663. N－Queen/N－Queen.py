global ans
ans = 0
n = int(input())
board = [[False for _ in range(n)] for _ in range(n)]

check1 = [False for _ in range(n)]
check2 = [False for _ in range(2*n-1)]  # 우상향 대각선: x+y
check3 = [False for _ in range(2*n-1)]  # 우하향 대각선: x-y+n-1

def sol(row):
    global ans
    
    if row >= n:
        ans += 1
        return
    
    for i in range(n):
        if not (board[row][i] or check1[i] or check2[row+i] or check3[i-row+n-1]):
            board[row][i] = True
            check1[i], check2[row+i], check3[i-row+n-1] = True, True, True
            sol(row+1)
            board[row][i] = False
            check1[i], check2[row+i], check3[i-row+n-1] = False, False, False

sol(0)
print(ans)