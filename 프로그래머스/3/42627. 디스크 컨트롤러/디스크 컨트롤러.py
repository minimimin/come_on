def solution(jobs):
    answer = 0  # 작업요청부터 종료까지 걸린 총시간
    # 소요 시간 오름차순 정렬
    n = len(jobs)
    sorted_list = sorted(jobs, key=lambda x: x[1])

    start = 0 #현재시간
    while sorted_list:
        for i in range(len(sorted_list)):
            # 작업 시점이 start보다 작거나같으면 작업시작하기
            if sorted_list[i][0] <= start:
                start += sorted_list[i][1]
                answer += start - sorted_list[i][0]
                sorted_list.pop(i)
                break
            

        else: # 반복문을 모두 돌았을 경우에도 시작하는 시간이없다면 시간을 1증가
            start += 1

    return answer // n