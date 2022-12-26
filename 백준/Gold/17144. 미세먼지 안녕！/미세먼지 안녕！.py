import sys; input = sys.stdin.readline

def dust(room, r, c):
    new_room = [[0 for _ in range(c)] for _ in range(r)]
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    
    for y in range(r):
        for x in range(c):
            if room[y][x] == -1:
                new_room[y][x] = -1
                continue
            
            cnt = 0
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                
                if not (0<=ny<r and 0<=nx<c):
                    continue
                
                if room[ny][nx] == -1:
                    continue
                
                cnt += 1
                new_room[ny][nx] += room[y][x]//5
            new_room[y][x] += room[y][x] - cnt * (room[y][x]//5)
    
    return new_room


def purifier(room, r, c):
    # 공기청정기 찾기
    m1, m2 = 0, 0
    for y in range(r):
        if room[y][0] == -1:
            m1, m2 = y, y+1
            break
    
    # 위쪽 공기청정기의 순환
    for y in range(m1-1, 0, -1):
        room[y][0] = room[y-1][0]
    
    for x in range(0, c-1, 1):
        room[0][x] = room[0][x+1]
    
    for y in range(0, m1, 1):
        room[y][c-1] = room[y+1][c-1]
    
    for x in range(c-1, 0, -1):
        room[m1][x] = room[m1][x-1]
        if x == 1:
            room[m1][x] += 1
        
    # 아래쪽 공기청정기의 순환
    for y in range(m2+1, r-1, 1):
        room[y][0] = room[y+1][0]
        
    for x in range(0, c-1, 1):
        room[r-1][x] = room[r-1][x+1]
    
    for y in range(r-1, m2, -1):
        room[y][c-1] = room[y-1][c-1]
    
    for x in range(c-1, 0, -1):
        room[m2][x] = room[m2][x-1]
        if x == 1:
            room[m2][x] += 1
            
    return room
    
r, c, t = map(int, input().split())
room = []

for _ in range(r):
    row = list(map(int, input().split()))
    room.append(row)

for _ in range(t):
    room = dust(room, r, c)
    room = purifier(room, r, c)

ans = 0
for y in range(r):
    for x in range(c):
        ans += room[y][x]
        
print(ans + 2)