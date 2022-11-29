n = int(input())
room = []
a, b = 0, 0
temp = []


for i in range(n):
    room.append(input())

if n == 1:
    print(0, 0)
    exit()

for i in range(n):
    if len(temp) > 1:
        a += 1
    temp = []
    for j in range(n):
        if room[i][j] == '.':
            temp.append(room[i][j])
        else:
            if len(temp) > 1:
                a += 1
            temp = []
if len(temp) > 1:
    a += 1
temp = []

for i in range(n):
    if len(temp) > 1:
        b += 1
    temp = []
    for j in range(n):
        if room[j][i] == '.':
            temp.append(room[j][i])
        else:
            if len(temp) > 1:
                b += 1
            temp = []
if len(temp) > 1:
    b += 1
        
print(a, b)
        
