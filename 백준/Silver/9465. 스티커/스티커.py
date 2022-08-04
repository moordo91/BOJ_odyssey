import sys; gets = sys.stdin.readline

def sol(n):
    row1 = list(map(int, gets().split()))
    row2 = list(map(int, gets().split()))
    mat = [[0 for _ in range(5)] for _ in range(n)]
    mat[0][0], mat[0][1] = row1[0], row2[0]

    for i in range(1, n):

        mat[i][0] = max(mat[i-1][1], mat[i-1][4]) + row1[i]
        mat[i][1] = max(mat[i-1][0], mat[i-1][3]) + row2[i]
        mat[i][2] = max(mat[i-1])
        if i >= 2:
            mat[i][3] = max(mat[i-2]) + row1[i]
            mat[i][4] = max(mat[i-2]) + row2[i]

    return max(mat[-1])

t = int(gets())

ans = []

for _ in range(t):
    ans.append(sol(int(gets())))

for i in ans:
    print(i)

