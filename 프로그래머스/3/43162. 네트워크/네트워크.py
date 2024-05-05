def dfs(k, n, visited, computers):
    visited[k] = 1
    for i in range(n):
        if not visited[i] and computers[k][i]:
            dfs(i, n, visited, computers)
            
def solution(n, computers):
    visited = [0] * n
    count = 0
    for i in range(n):
        if not visited[i]:
            count += 1
            dfs(i, n, visited, computers)
    return count