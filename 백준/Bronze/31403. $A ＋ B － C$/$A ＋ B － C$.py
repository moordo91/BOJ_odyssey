import sys
input = sys.stdin.readline

k = []
for i in range(3):
    k.append(int(input()))

print(k[0]+k[1]-k[2])
print(int(str(k[0])+str(k[1]))-k[2])
