n = int(input())
n = 4*n-3

for i in range(n//2):
    if i % 2 == 0:
        print("* "*(i//2) + "*"*(n-2*i) + " *"*(i//2))
    else:
        print("* "*((i+1)//2) + " "*(n-(i+1)*2) + " *"*((i+1)//2))
for i in range(n):
    if i % 2 == 0:
        print("*", end='')
    else:
        print(" ", end='')
print()
for i in range(n//2-1, -1, -1):
    if i % 2 == 0:
        print("* "*(i//2) + "*"*(n-2*i) + " *"*(i//2))
    else:
        print("* "*((i+1)//2) + " "*(n-(i+1)*2) + " *"*((i+1)//2))