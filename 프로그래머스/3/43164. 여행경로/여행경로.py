def find_route(answer, tickets, visited, start, ticket_count):
    # 모든 항공권을 사용한 경우
    if len(answer) == ticket_count + 1:
        return list(answer)
    
    # 항공권을 알파벳 순으로 탐색
    for i in range(len(tickets)):
        if tickets[i][0] == answer[-1] and not visited[i]:
            visited[i] = True
            answer.append(tickets[i][1])
            result = find_route(answer, tickets, visited, i, ticket_count)
            if result:
                return result
            visited[i] = False
            answer.pop()
    
    return None

def solution(tickets):
    tickets.sort()  # 알파벳 순으로 정렬
    visited = [False] * len(tickets)
    return find_route(['ICN'], tickets, visited, 0, len(tickets))
