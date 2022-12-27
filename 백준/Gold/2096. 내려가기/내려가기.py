import sys; intput = sys.stdin.readline

def max_min(arr):
    max_val = max(list(map(max, arr)))
    min_val = min(list(map(min, arr)))
    return max_val, min_val

def sol(line_buffer, new_line):
    new_line_buffer = [[new_line[i]] * 2 for i in range(3)]
    max_val, min_val = max_min(line_buffer[:2])
    new_line_buffer[0][0] += max_val
    new_line_buffer[0][1] += min_val
    max_val, min_val = max_min(line_buffer[:])
    new_line_buffer[1][0] += max_val
    new_line_buffer[1][1] += min_val
    max_val, min_val = max_min(line_buffer[1:])
    new_line_buffer[2][0] += max_val
    new_line_buffer[2][1] += min_val
    
    return new_line_buffer
    

n = int(input())
a, b, c = map(int, input().split())
line_buffer = [[a, a], [b, b], [c, c]]

for _ in range(n-1):
    new_line = list(map(int, input().split()))
    line_buffer = sol(line_buffer, new_line)

max_val, min_val = max_min(line_buffer)
print(max_val, min_val)