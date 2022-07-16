import heapq as hq
import sys

ipt = sys.stdin.readline

def sync(heap, tag):
    while heap and not tag[heap[0][1]]:
        hq.heappop(heap)

def sol(k):
    minH = []
    maxH = []
    tag = [False] * 1000000
    for i in range(k):
        cmd, num = ipt().split()
        num = int(num)
        
        if cmd == 'I':
            hq.heappush(minH, (num, i))
            hq.heappush(maxH, (-num, i))
            tag[i] = True
        
        else:
            if num == 1:
                sync(maxH, tag)
                if maxH:
                    tag[maxH[0][1]] = False
                    hq.heappop(maxH)
            elif num == -1:
                sync(minH, tag)
                if minH:
                    tag[minH[0][1]] = False
                    hq.heappop(minH)
    
    sync(maxH, tag)
    sync(minH, tag)

    if len(minH) == 0:
        print("EMPTY")
    else:
        print(-maxH[0][0], minH[0][0])

T = int(ipt())
for _ in range(T):
    sol(int(ipt()))