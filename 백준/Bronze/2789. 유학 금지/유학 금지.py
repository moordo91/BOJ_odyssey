import copy

cambridge = ['C', 'A', 'M', 'B', 'R', 'I', 'D', 'G', 'E']
q = input()
p = list(copy.deepcopy(q))
for i in q:
    if i in cambridge:
        p.remove(i)

for i in p:
    print(i, end='')