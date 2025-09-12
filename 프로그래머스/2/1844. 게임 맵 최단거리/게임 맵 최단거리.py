from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[0]*m for _ in range(n)]
    directions = [(0,+1), (0,-1), (+1,0), (-1,0)]
    
    if maps[0][0] == 1:
        moving = deque([(0,0)])
        visited[0][0] = 1
    
    while moving:
        x, y = moving.popleft()
        if x == n-1 and y == m-1:
            return visited[x][y]
        
        for rl, ud in directions:
            if 0 <= x+rl < n and 0 <= y+ud < m and not visited[x+rl][y+ud] and maps[x+rl][y+ud]:
                visited[x+rl][y+ud] = visited[x][y] + 1
                moving.append((x+rl, y+ud))
    return -1