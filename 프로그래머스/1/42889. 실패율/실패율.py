def solution(N, stages):
    # 스테이지별 실패한 사람 수
    fail_person = [0]*(N+1)
    for person in stages:
        if person > N:
            continue
        fail_person[person] += 1

    # 스테이지별 실패율
    mans_cnt = len(stages)
    fail_percent = [0]*(N+1)
    for stage in range(N):
        if fail_person[stage+1] == 0: 
            fail_percent[stage+1] = 0
            continue
        fail_percent[stage+1] = fail_person[stage+1]/mans_cnt
        mans_cnt -= fail_person[stage+1]
    # lambda식 활용을 위해 딕셔너리로 만들기
    # fail_percent = {}
    # for stage in range(N):
    #     if fail_person[stage+1] == 0:
    #         fail_percent[stage+1] = 0
    #         continue
    #     fail_percent[stage+1] = fail_person[stage+1]/mans_cnt
    #     mans_cnt -= fail_person[stage+1]

    # 실패율이 높은 스테이지순으로 반환
    stage_per = []
    for idx, per in enumerate(fail_percent):
        if idx == 0:
            continue
        stage_per.append((per,idx))
    # print(stage_per)
    # stage_per.sort(reverse=True)
    # print(stage_per)
    # answer = [stg for per, stg in stage_per]
    stage_per.sort(key=lambda x: x[0], reverse=True)
    return [stg for per, stg in stage_per]
    # lambda식 활용 <= 딕셔너리 사용하기!!
    # return sorted(fail_percent, key=lambda x : fail_percent[x], reverse=True)