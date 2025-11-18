from collections import deque

def solution(cards1, cards2, goal):
    # 순서대로 한장씩 사용!
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    goal = deque(goal)
    answer = True
    while goal:
        std = goal.popleft()
        if cards1:
            wd1 = cards1.popleft()
            if wd1 != std:
                cards1.appendleft(wd1)
                answer = False
            else:
                answer = True
                continue
        if cards2:
            wd2 = cards2.popleft()
            if wd2 != std:
                answer = False
                cards2.appendleft(wd2 )
            else:
                answer = True
                continue
        if not answer:
            return "No"
    return "Yes"