def find_num(alpha, number):
    if alpha in number:
        return number[alpha]
    return 'No'

def solution(s):
    answer = []
    number = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    alpha = ''
    for i in s:
        if str(i).isdigit():
            answer.append(i)
        else:
            alpha += i
            if str(find_num(alpha, number)).isdigit():
                answer.append(find_num(alpha, number))
                alpha = ''
    real_answer = ''
    for num in answer:
        real_answer += str(num)
    return int(real_answer)