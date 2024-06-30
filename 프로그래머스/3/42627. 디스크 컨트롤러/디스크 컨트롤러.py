# 작업 순서대로 들어온다 [요청 시점, 작업 소요 시간]
# 첫번째 작업 시간 안에 들어가는 애들이면 일단 임시 저장소에 다 넣어놓고 빠른 순서대로 진행시키기
# 하드디스크가 작업을 수행하고 있지 않을 때에는 먼저 요청이 들어온 작업부터 처리합니다.라는 조건이 있으니까 그 시간 안에 하는 게 아니라면 바로 실행시키기
# answer에는 걸린 시간들 넣기

import heapq
from collections import deque

def solution(jobs):
    answer = deque()
    heapq.heapify(jobs)
    first_wait, first_work = heapq.heappop(jobs)
    time = first_wait + first_work
    start_time = first_wait
    answer.append(time - start_time)
    temp = []
    
    while jobs or temp:
        while jobs and jobs[0][0] <= time:
            waiting_time, working_time = heapq.heappop(jobs)
            heapq.heappush(temp, [working_time, waiting_time])
        if temp:
            work, wait = heapq.heappop(temp)
            time += work
            start_time = wait
            answer.append(time - start_time)
        elif jobs:
            waiting_time, working_time = heapq.heappop(jobs)
            time = waiting_time + working_time
            start_time = waiting_time 
            answer.append(working_time)
    return sum(answer)//len(answer)