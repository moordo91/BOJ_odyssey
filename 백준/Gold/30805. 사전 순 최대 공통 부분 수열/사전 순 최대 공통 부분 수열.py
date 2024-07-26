import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

x = 100
ans = []

def check(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            max_idx = i
            return max_idx
    return -1
              
while x > 0:
    max_idx_a = check(a, x)
    max_idx_b = check(b, x)
    if max_idx_a >= 0 and max_idx_b >= 0:
        ans.append(x)
        a = a[max_idx_a+1:]
        b = b[max_idx_b+1:]
        x += 1
    else:
        x -= 1

print(len(ans))
for i in ans:
    print(i, end=' ')
print()