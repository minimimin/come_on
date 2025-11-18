from collections import deque

def solution(progresses, speeds):
    # 진도가 100일때 배포
    # 개발은 먼저 되더라도 앞 기능이 배포될때 배포되어야 함
    # 작업순서별 진도, 작업 개발속도
    # 각 배포마다 배포되는 기능 수 반환
    finish_pg = []
    new_progresses = deque(progresses)
    new_speeds = deque(speeds)
    while new_progresses:
        temp_cnt = 0
        while new_progresses:
            if new_progresses[0] >= 100:
                new_progresses.popleft()
                new_speeds.popleft()
                temp_cnt += 1
            else:
                break
        if temp_cnt:
            finish_pg.append(temp_cnt)
        if new_speeds:
            for i in range(len(new_speeds)):
                new_progresses[i] += new_speeds[i]
    return finish_pg