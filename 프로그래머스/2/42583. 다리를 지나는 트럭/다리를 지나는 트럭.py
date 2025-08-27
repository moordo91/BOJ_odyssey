from collections import deque

def solution(bridge_length, weight, truck_weights):
    N = len(truck_weights)
    end_truck = deque([])
    going_truck = deque([])
    wait_truck = deque(truck_weights)
    max_weight = weight
    remain_length = bridge_length
    answer = 0
    
    while len(end_truck) < N:
        going_truck = deque([(w, r_l-1) for w, r_l in going_truck])
        if going_truck and going_truck[0][1] == 0:
            w, _ = going_truck.popleft()
            weight += w
            remain_length += 1
            end_truck.append(w)
        
        if wait_truck:
            if remain_length and weight >= wait_truck[0]:
                w = wait_truck.popleft()
                going_truck.append((w, bridge_length))
                weight -= w
                remain_length -= 1
        answer += 1
    return answer