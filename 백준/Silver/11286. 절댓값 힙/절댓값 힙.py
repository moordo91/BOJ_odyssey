import heapq as hq
import sys; gets = sys.stdin.readline

heap = []
n = int(gets())

for _ in range(n):
    num = int(gets())
    if num != 0:
        if num > 0:
            hq.heappush(heap, (num, 1))
        else:
            hq.heappush(heap, (-num, 0))
    else:
        if not heap:
            print(0)
        else:
            tmp = hq.heappop(heap)
            if tmp[1] > 0:
                print(tmp[0])
            else:
                print(-tmp[0])