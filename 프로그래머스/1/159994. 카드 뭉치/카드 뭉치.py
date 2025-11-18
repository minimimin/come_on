from collections import deque

def solution(cards1, cards2, goal):
    goal = deque(goal)
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    while goal:
        if cards1 and cards1[0] == goal[0]:
            goal.popleft()
            cards1.popleft()
            continue
        elif cards2 and cards2[0] == goal[0]:
            goal.popleft()
            cards2.popleft()
            continue
        else:
            return "No"
    # return "Yes" if not goal and not cards1 and not cards2 else "No"
    return "Yes"