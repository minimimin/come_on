from collections import deque

def bfs(start, transmission_tower, visited):
    queue = deque([start])
    visited[start] = 1
    count = 1
    while queue:
        node = queue.popleft()
        for new_node in transmission_tower[node]:
            if not visited[new_node]:
                visited[new_node] = 1
                queue.append(new_node)
                count += 1
    return count

def solution(n, wires):
    answer = 100
    all_wire = deque(wires)
    for i in range(n):
        temp = all_wire.popleft()
        
        transmission_tower = [[] for _ in range(n+1)]
        visited = [0] * (n+1)
        
        for wire in all_wire:
            transmission_tower[wire[0]].append(wire[1])
            transmission_tower[wire[1]].append(wire[0])
        
        # 끊어진 전력망에서 첫번째 그룹의 크기 구하기
        cnt = bfs(1, transmission_tower, visited)
        
        # 두 그룹 간 차이 계산(나머지 한 그룹의 크기 = n - cnt)
        # for문 도는 동안 제일 작은 값이 최소 차이
        answer = min(answer, abs(cnt*2 - n))
        
        all_wire.append(temp)
    return answer