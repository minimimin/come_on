from collections import deque

def solution(s):
    queue_s = deque(s)
    count = 0
    while queue_s:
        count = count + 1 if queue_s.popleft() == '(' else count - 1
        if count < 0:
            return False
    return not count