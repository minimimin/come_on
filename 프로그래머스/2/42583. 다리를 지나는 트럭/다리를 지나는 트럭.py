# 정해진 순서로 다리 건너기
# 전체 다리 길이, 올라갈 수 있는 무게, 대기트럭
# 건너는 데 다리 길이 초, 올라가는 건 1초당 하나씩! 다 지나오면 1초 더!

from collections import deque

def solution(bridge_length, weight, truck_weights):
    if len(truck_weights) == 1:
        return bridge_length + 1
    bridge = deque([0 for _ in range(bridge_length)])
    trucks = deque(truck_weights)
    total_weight = weight
    count = 0
    while trucks:
        total_weight += bridge.popleft()
        count += 1
        if total_weight >= trucks[0]:
            truck = trucks.popleft()
            bridge.append(truck)
            total_weight -= truck
        else:
            bridge.append(0)
    if not bridge == deque([0 for _ in range(bridge_length)]):
        while bridge:
            bridge.popleft()
            count += 1
    return count