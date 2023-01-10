n = int(input())
a = sorted(list(map(int, input().split())))

m = int(input())
b = list(map(int, input().split()))

for i in range(m):
    min_i = 0
    max_i = n-1
    switch = False
    
    if b[i] > a[max_i] or b[i] < a[min_i]:
        print(0)
        continue
    
    while min_i <= max_i:
        mid_i = (min_i + max_i) // 2
        if b[i] == a[mid_i]:
            switch = True
            print(1)
            break
        elif a[mid_i] < b[i]:
            min_i = mid_i + 1
        else:
            max_i = mid_i - 1
            
    if not switch:
        print(0)