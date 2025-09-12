def solution(tickets):
    visited = [0 for _ in range(len(tickets))]
    airports = ["ICN"]
    tickets.sort()

    def DFS():
        if len(airports) > len(tickets) and all(visited):
        # if len(airports) > len(tickets):
            print(airports)
            return airports
        for ticket_num in range(len(tickets)):
            if tickets[ticket_num][0] == airports[-1] and not visited[ticket_num]:
                visited[ticket_num] = 1
                airports.append(tickets[ticket_num][1])
                if DFS():
                    return airports
                airports.pop()
                visited[ticket_num] = 0

    if DFS():
        return airports