from collections import deque

def solution(bridge_length, weight, truck_weights):
    if len(truck_weights) == 1:
        return bridge_length + 1
    bridge = deque([0] * bridge_length)
    all_trucks = len(truck_weights)
    trunck_num = 0
    total_weight = weight
    count = 0
    while trunck_num < all_trucks:
        total_weight += bridge.popleft()
        count += 1
        truck = truck_weights[trunck_num]
        if total_weight >= truck:
            bridge.append(truck)
            total_weight -= truck
            trunck_num += 1
        else:
            bridge.append(0)
    return count + bridge_length