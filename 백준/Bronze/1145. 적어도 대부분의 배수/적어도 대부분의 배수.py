import math
from itertools import combinations

def gcd(arr):
    g = arr[0]
    for item in arr:
        g = math.gcd(g, item)
    return g

def lcm_N(arr):
    l = 1
    for item in arr:
        l = math.lcm(l, item)
    return l



arr = list(map(int, input().split()))
ans = []
for i in list(combinations(arr, 3)):
    ans.append(lcm_N(i))
    
print(min(ans))