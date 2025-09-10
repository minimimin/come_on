# 셋이 맞춘 점수 합계 구함..ㅎ...문제 똑바로 읽자!!
# 가장 많은 문제를 맞힌 사람이 누구인지 구하기!!
def solution(answers):
    answers_len = len(answers)
    collect_ans = {1:0, 2:0, 3:0}
    # 1번 1~5(5) 반복 / 2번 2,1,2,3,2,4,2,5(8) 반복 / 3번 3,3,1,1,2,2,4,4,5,5(10) 반복
    one_ans = [1,2,3,4,5]
    two_ans = [2,1,2,3,2,4,2,5]
    three_ans = [3,3,1,1,2,2,4,4,5,5]
    # 각 수포자들이 전체 제출한 답안
    fir_supo = one_ans*(answers_len//len(one_ans)) + one_ans[0:answers_len%len(one_ans)]
    sec_supo = two_ans*(answers_len//len(two_ans)) + two_ans[0:answers_len%len(two_ans)]
    three_supo = three_ans*(answers_len//len(three_ans)) + three_ans[0:answers_len%len(three_ans)]
    # 채점
    for num in range(answers_len):
        if fir_supo[num] == answers[num]:
            collect_ans[1] += 1
        if sec_supo[num] == answers[num]:
            collect_ans[2] += 1
        if three_supo[num] == answers[num]:
            collect_ans[3] += 1
    # 최종 점수비교 = 제일 큰 값을 우선 구해놓고, 그거랑 비교해서 같으면 정답에 넣기!
    max_collect = max(collect_ans.values())
    print(max_collect)
    answer = []
    for supo in collect_ans:
        if collect_ans[supo] == max_collect:
            answer.append(supo)
    return answer