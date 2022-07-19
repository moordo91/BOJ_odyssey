import sys
g=sys.stdin.readline
for _ in range(int(g())):
 a,b=map(int,g().split())
 print((b%a==0)*(b>a))