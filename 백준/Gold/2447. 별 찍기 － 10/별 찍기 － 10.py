n = int(input())

def sol(n):
    if n == 3:
        return ['***', '* *', '***']

    arr = sol(n//3)
    star = []

    for i in arr:
        star.append(i*3)
    for i in arr:
        star.append(i + ' '*(n//3) + i)
    for i in arr:
        star.append(i*3)
    
    return star

print('\n'.join(sol(n)))