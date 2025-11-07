from collections import Counter

def solution(N, stages):
    answer = {}
    peopleCnt = len(stages)
    stageFailCnt = Counter(stages)
    for stage in range(1,N+1):
        if stage not in stageFailCnt:
            answer[stage] = 0
            continue
        answer[stage] = stageFailCnt[stage]/peopleCnt
        peopleCnt -= stageFailCnt[stage]
    return sorted(answer, key=lambda x : answer[x], reverse=True)