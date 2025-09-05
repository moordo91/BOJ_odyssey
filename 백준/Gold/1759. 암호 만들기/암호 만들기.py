import sys
from itertools import combinations
input = sys.stdin.readline

L, C = map(int, input().split())
chars = list(map(str, input().split()))
chars.sort()

aeiou = set([])
abc = set([])
for i, c in enumerate(chars):
    if c in ['a', 'e', 'i', 'o', 'u']:
        aeiou.add(i)
    else:
        abc.add(i)

for comb in combinations(range(C), L):
    if len(aeiou & set(comb)) == 0 or len(set(comb) - aeiou) < 2:
        continue
    for c in sorted(comb):
        print(chars[c], end='')
    print()