import sys

def sol(order, s):
    if order[:-1] == "all":
        tmp = [i for i in range(1, 20+1)]
        s = set(tmp)
    elif order[:-1] == "empty":
        s = set([])
    else:
        odr, num = map(str, order.split())
        if odr == "add" and int(num) not in s:
            s.add(int(num))
        elif odr == "remove":
            if len(s) > 0 and int(num) in s:
                s.remove(int(num))
        elif odr == "check":
            if int(num) in s:
                print(1)
            else:
                print(0)
        elif odr == "toggle":
            if int(num) in s:
                s.remove(int(num))
            else:
                s.add(int(num))
    return s

m = int(sys.stdin.readline())
s = set([])
for i in range(m):
    order = sys.stdin.readline()
    s = sol(order, s)