def solution(answers):
#     1번 : 1~5 반복
#     2번 : 2, 1, 2, 3, 2, 4, 2, 5 반복
#     3번 : 3, 3, 1, 1, 2, 2, 4, 4, 5, 5 반복
# 일단 for문 돌리고, 딕셔너리 만들어서 담을까?
# 아 근데 그러면 1,2,3은 어떻게 체크하지?
    one = [1,2,3,4,5] * (len(answers)//3)
    two = [2, 1, 2, 3, 2, 4, 2, 5] * (len(answers)//3)
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (len(answers)//3)
    # answer = {1:0,2:0,3:0}
    answer = [0,0,0]
    for i in range(len(answers)):
        if answers[i] == one[i]:
            answer[0] += 1
        if answers[i] == two[i]:
            answer[1] += 1
        if answers[i] == three[i]:
            answer[2] += 1
    real_answer = []
    for j in range(len(answer)):
        if answer[j] == max(answer):
            real_answer.append(j+1)
    return real_answer