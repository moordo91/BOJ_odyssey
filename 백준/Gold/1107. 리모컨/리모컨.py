START = 100
button = set([])

target = int(input())
n = int(input())
if n:
    button = set(list(map(int, input().split())))

def sol(target, button):
    i = 0
    d = abs(target - START)
    while 1:
        ans = [d]
        if i >= d:
            return d
        else:
            switch = False
            if not (set(list(map(int, str(target+i)))) & button):
                ans.append(len(str(target+i)) + i)
                switch = True
            if i <= target:
                if not (set(list(map(int, str(target-i)))) & button):
                    ans.append(len(str(target-i)) + i)
                    switch = True
            if switch:
                return min(ans)
        i += 1

print(sol(target, button))