def solution(answers):
    # 전체 정답 길이
    # all_answer = len(answers)
    # 각 수포자들 답지
    # num_one = [1,2,3,4,5]
    # num_two = [2,1,2,3,2,4,2,5]
    # num_three = [3,3,1,1,2,2,4,4,5,5]
    supos_answers = [
        [1,2,3,4,5],
        [2,1,2,3,2,4,2,5],
        [3,3,1,1,2,2,4,4,5,5]
    ]
    # 수포자들 정답개수
    cnt = [0,0,0]
    # 채점
    # for answer_num in range(all_answer):
    #     if answers[answer_num] == num_one[answer_num%len(num_one)]:
    #         cnt[0] += 1
    #     if answers[answer_num] == num_two[answer_num%len(num_two)]:
    #         cnt[1] += 1
    #     if answers[answer_num] == num_three[answer_num%len(num_three)]:
    #         cnt[2] += 1
    for i, answer in enumerate(answers):
        for j, supo_answer in enumerate(supos_answers):
            if answers[i] == supo_answer[i%len(supo_answer)]:
                cnt[j] += 1
    # 누가 제일 많이 맞췄는지 확인
    winner = []
    big_point = max(cnt)
    for supo in range(3):
        if cnt[supo] == big_point:
            winner.append(supo+1)
    return winner