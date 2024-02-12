import sys, statistics
input = sys.stdin.readline

def round(x):
    if x - int(x) >= 0.5:
        return int(x) + 1
    return int(x)

n = int(input())
if n == 0:
    print(0)
    exit()
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()
e = int(round(n * 0.15))
arr = arr[e:n-e]
print(int(round(statistics.mean(arr))))
