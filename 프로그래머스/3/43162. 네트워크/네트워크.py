from collections import deque

def solution(n, computers):
    visited = [0]*n
    count = 0
    check = deque([])

    for network in range(n):
        if not visited[network]:
            visited[network] = 1
            check.append(network)
            while check:
                now_net = check.popleft()
                for next_net in range(n):
                    if not visited[next_net] and computers[now_net][next_net]:
                        visited[next_net] = 1
                        check.append(next_net)
            count += 1
                
    return count