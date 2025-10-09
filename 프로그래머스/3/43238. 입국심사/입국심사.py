def solution(n, times):
    answer = 0
    # 이분탐색은 정렬한 상태에서 시작이지만, 지금은 기준이 시간이기에 심사대를 정렬할 필요는 없음!
    # 그렇지만 심사대 시간 순서로 확인할거라서 필요하지 않을까?
    times.sort()
    min_time = times[0]
    max_time = min_time*n
    # 시간을 기준으로 가능한 여부 나눠서 보기
    while min_time <= max_time:
        avg_time = (min_time + max_time) // 2
        how_many_simsa = 0
        for simsa_time in times:
            how_many_simsa += avg_time//simsa_time
            if how_many_simsa >= n:
                max_time = avg_time-1
                answer = avg_time
                break
            # elif how_many_simsa == n:
            #     return answer
        else:
            min_time = avg_time+1
    return answer