n = int(input())
a = 0

arr = input()

for i in range(n):
    if arr[i] == 'A':
        a += 1

if a > n/2:
    print('A')
elif a < n/2:
    print('B')
else:
    print('Tie')