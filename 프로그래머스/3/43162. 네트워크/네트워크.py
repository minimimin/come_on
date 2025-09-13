def solution(n, computers):
    visited = [0]*n
    count = [0]
    
    def dfs(i):
        for j in range(n):
            if not visited[j] and computers[i][j]:
                visited[j] = 1
                dfs(j)

        # else:
        #     count[0] += 1
                
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            dfs(i)
            count[0] += 1
    return count[0]