n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
answer = [0, 0]

def sol(x, y, n):
    color = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != paper[i][j]:
                sol(x, y, n//2)
                sol(x, y + n//2, n//2)
                sol(x + n//2, y, n//2)
                sol(x + n//2, y + n//2, n//2)
                return
    
    if color == 0:
        answer[0] += 1
    else:
        answer[1] += 1

sol(0, 0, n)
for num in answer:
    print(num)