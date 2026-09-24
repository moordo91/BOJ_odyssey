from collections import deque

N, M, K = map(int, input().split())

sea = [list(map(int, input().split())) for _ in range(N)]

turtles = []
for _ in range(M):
    r, c = map(int, input().split())
    turtles.append([r, c])

volcanoes = []
for _ in range(K):
    r, c, p = map(int, input().split())
    volcanoes.append([r, c, p, 0])  # r, c, threshold, pressure


# 우, 하, 좌, 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

DEST = (N - 1, N - 1)

alive = [True] * M
answer = [-1] * M
fossils = set()


def find_first_move(turtle_id):
    sr, sc = turtles[turtle_id]

    occupied = fossils.copy()

    for i in range(M):
        if i != turtle_id and alive[i]:
            occupied.add(tuple(turtles[i]))

    visited = [[False] * N for _ in range(N)]
    visited[sr][sc] = True

    # r, c, 처음 이동한 방향
    q = deque()

    for d in range(4):
        nr = sr + dr[d]
        nc = sc + dc[d]

        if not (0 <= nr < N and 0 <= nc < N):
            continue
        if sea[nr][nc] == 1:
            continue
        if (nr, nc) in occupied:
            continue

        visited[nr][nc] = True
        q.append((nr, nc, d))

    while q:
        r, c, first_dir = q.popleft()

        if (r, c) == DEST:
            return first_dir

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if not (0 <= nr < N and 0 <= nc < N):
                continue
            if visited[nr][nc]:
                continue
            if sea[nr][nc] == 1:
                continue
            if (nr, nc) in occupied:
                continue

            visited[nr][nc] = True
            q.append((nr, nc, first_dir))

    return -1


def move_turtles(turn):
    for i in range(M):
        if not alive[i]:
            continue

        direction = find_first_move(i)

        if direction == -1:
            continue

        r, c = turtles[i]
        nr = r + dr[direction]
        nc = c + dc[direction]

        turtles[i] = [nr, nc]

        if (nr, nc) == DEST:
            alive[i] = False
            answer[i] = turn


def spread_heat(sr, sc, start_heat, total_heat):
    visited = [[False] * N for _ in range(N)]
    visited[sr][sc] = True

    q = deque([(sr, sc, start_heat)])

    while q:
        r, c, heat = q.popleft()

        total_heat[r][c] += heat

        next_heat = heat // 2

        if next_heat == 0:
            continue

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if not (0 <= nr < N and 0 <= nc < N):
                continue
            if visited[nr][nc]:
                continue
            if sea[nr][nc] == 1:
                continue

            visited[nr][nc] = True
            q.append((nr, nc, next_heat))


def erupt():
    total_heat = [[0] * N for _ in range(N)]
    erupted = [False] * K

    q = deque()

    # 최초 분출
    for i in range(K):
        r, c, p, pressure = volcanoes[i]

        if pressure >= p:
            erupted[i] = True
            q.append(i)

    # 연쇄 분출
    while q:
        idx = q.popleft()

        r, c, p, pressure = volcanoes[idx]

        spread_heat(r, c, p, total_heat)

        # 새로 임계치를 넘은 화산 탐색
        for i in range(K):
            if erupted[i]:
                continue

            vr, vc, vp, vpressure = volcanoes[i]

            if vpressure + total_heat[vr][vc] >= vp:
                erupted[i] = True
                q.append(i)

    return total_heat, erupted


def fossilize(total_heat):
    for i in range(M):
        if not alive[i]:
            continue

        r, c = turtles[i]

        if total_heat[r][c] >= 20:
            alive[i] = False
            fossils.add((r, c))


for turn in range(1, 101):
    # 1. 거북이 이동
    move_turtles(turn)

    # 전부 도착했다면 종료 가능
    if all(not alive[i] for i in range(M)):
        break

    # 2. 모든 화산 압력 +10
    for volcano in volcanoes:
        volcano[3] += 10

    # 3. 분출 + 연쇄 반응
    total_heat, erupted = erupt()

    # 거북이 화석화
    fossilize(total_heat)

    # 4. 이번 턴 분출 화산의 압력 초기화
    for i in range(K):
        if erupted[i]:
            volcanoes[i][3] = 0


for result in answer:
    print(result)