from collections import deque

def solution(people, limit):
    people.sort(reverse=True)
    cnt = 0
    people_queue = deque(people)
    while people_queue:
        boat = limit - people_queue.popleft()
        if people_queue:
            slim_man = people_queue.pop()
            if boat < slim_man:
                people_queue.append(slim_man)
            else:
                boat -= slim_man
        # while people_queue:
        #     slim_man = people_queue.pop()
        #     if boat < slim_man:
        #         people_queue.append(slim_man)
        #         break
        #     else:
        #         boat -= slim_man
        cnt += 1
    return cnt