from collections import deque

directions = {
    1: [(-1, 0), (0, -1), (0, 1), (1, 0)],
    2: [(1, 0), (0, 1), (0, -1), (-1, 0)],
    3: [(0, -1), (1, 0), (-1, 0), (0, 1)],
    4: [(0, 1), (-1, 0), (1, 0), (0, -1)]
}

directions_ = {
    (-1, 0): 1,
    (1, 0): 2,
    (0, -1): 3,
    (0, 1): 4
}

JUMP_ORDERS = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def move(N, r, c, d, grid, answer):
    jump_flag = False
    len_answer = len(answer) - 1
    while not jump_flag:
        len_answer += 1
        for i in range(4):
            dr, dc = directions[d][i]
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] == 0:
                grid[nr][nc] = 2
                answer.append((nr, nc))
                r, c = nr, nc
                d = directions_[(dr, dc)]
                break
        if len(answer) == len_answer:
            jump_flag = True
    return r, c, d


def jump(N, r, c, grid):
    queue = deque([(r, c, 0)])
    visited = {(r, c)}
    candis = []
    nearest_level = 1_000_000
    while queue:
        r, c, l = queue.popleft()
        if l > nearest_level:
            break
        for dr, dc in JUMP_ORDERS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] != 1 and (nr, nc) not in visited:
                queue.append((nr, nc, l + 1))
                visited.add((nr, nc))
                if grid[nr][nc] == 0 and l + 1 <= nearest_level:
                    nearest_level = min(nearest_level, l + 1)
                    d = directions_[(dr, dc)]
                    candis.append((nr, nc, d))
    return candis


def main(N, r, c, d, grid):
    r, c = r - 1, c - 1
    grid[r][c] = 2
    answer = deque([(r, c)])
    while True:
        r, c, d = move(N, r, c, d, grid, answer)
        candis = jump(N, r, c, grid)
        if len(candis) == 0:
            return answer
        candis.sort()
        r, c, d = candis[0]
        grid[r][c] = 2
        answer.append((r, c))


def print_ans(answer):
    for y, x in answer:
        print(f"{y + 1} {x + 1}")


if __name__ == "__main__":
    N, r, c, d = map(int, input().split())
    grid = []
    for _ in range(N):
        row = list(map(int, input().split()))
        grid.append(row)
    ANSWER = main(N, r, c, d, grid)
    print_ans(ANSWER)
