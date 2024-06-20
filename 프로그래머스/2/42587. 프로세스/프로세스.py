from collections import deque

def solution(priorities, location):
    pri_que = deque([(priorities[i], i) for i in range(len(priorities))])
    count = 0
    while pri_que:
        current = pri_que.popleft()
        if any(current[0] < q[0] for q in pri_que):
            pri_que.append(current)
        else:
            count += 1
            if current[1] == location:
                return count