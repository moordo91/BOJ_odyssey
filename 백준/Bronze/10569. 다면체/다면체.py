def sol(v, e):
    return 2 + e - v
    
t = int(input())
for _ in range(t):
    v, e = map(int, input().split())
    print(sol(v, e))