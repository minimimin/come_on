# 작업의 진도(<100), 작업의 개발속도(<=100)
# 각 배포마다 몇 개의 기능이 배포되는지?
# 개발 순서는 상관없지만, 배포는 앞에 거 배포될때 뒤에꺼 배포될 수 있음
# 배포는 하루 한 번만, 하루 끝에!

# 하루에 각각 speeds만큼 +하는데, 100이 되면 멈추고, 100이 안되면 계속 더해주기
# 배포할때(함수 마지막에) 100인거 빼낼건데 맨 앞이 100이 아니면 뒤에거도 못꺼냄
# 앞에거부터 함수에 담아놓기

from collections import deque

def solution(progresses, speeds):    
    answer = deque()
    while progresses:
        count = 0
        for i in range(len(progresses)):
            if progresses[i] == 100:
                continue
            elif progresses[i] + speeds[i] >= 100:
                progresses[i] = 100
            else:
                progresses[i] += speeds[i]
        while progresses and progresses[0] == 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        if count > 0:
            answer.append(count)
    return list(answer)