q = [0, 0, 0, 0, 0]

def sol(x, y):
    if x > 0 and y > 0:
        q[0] += 1
    elif x < 0 and y > 0:
        q[1] += 1
    elif x < 0 and y < 0:
        q[2] += 1
    elif x > 0 and y < 0:
        q[3] += 1
    else:
        q[4] += 1

n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    sol(x, y)

for i in range(4):
    print(f"Q{i+1}: {q[i]}")
print(f"AXIS: {q[4]}")