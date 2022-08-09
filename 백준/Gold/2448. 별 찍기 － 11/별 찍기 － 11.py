n = int(input())

def sol(n):
    if n == 3:
        return ['  *  ', ' * * ', '*****']
    
    arr = sol(n//2)
    star = []

    for i in arr:
        star.append(' '*(n//2) + i + ' '*(n//2))
    for i in arr:
        star.append(i + ' ' + i)

    return star

print('\n'.join(sol(n)))