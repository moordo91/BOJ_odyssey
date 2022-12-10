def sol():
    n = int(input())
    total_gpa = []
    total_p = 0
    for _ in range(n):
        c, p = map(float, input().split())
        total_gpa.append(c*p)
        total_p += c
    print(f"{int(total_p)} {sum(total_gpa)/total_p:.01f}")


t = int(input())
for _ in range(t):
    sol()
