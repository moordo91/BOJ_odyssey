def solution(n, times):
    times.sort()
    lo, hi = 0, min(times) * n
    while lo < hi:
        mid = (lo + hi) // 2
        done = sum(mid // t for t in times)
        if done >= n:
            hi = mid
        else:
            lo = mid + 1
    return lo