t = int(input())

def sol(arr):
    ans = 0
    op = ['@', '%', '#']
    for item in arr:
        if item not in op:
            ans += float(item)
        else:
            if item == op[0]:
                ans *= 3
            elif item == op[1]:
                ans += 5
            else:
                ans -= 7
    return ans


for _ in range(t):
    equ = list(map(str, input().split()))
    print(f"{sol(equ):.2f}")