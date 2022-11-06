import math

n, k = map(int, input().split())
student = [[0, 0] for _ in range(6)]
ans = 0

for _ in range(n):
    s, y = map(int, input().split())
    student[y-1][s] += 1

for i in range(6):
    for j in range(2):
        ans += math.ceil(student[i][j] / k)

print(ans)