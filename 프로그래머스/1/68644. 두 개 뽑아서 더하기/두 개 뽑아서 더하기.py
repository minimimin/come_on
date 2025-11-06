def solution(numbers):
    len_num = len(numbers)
    set_answer = set()
    for i in range(len_num-1):
        for j in range(i+1,len_num):
            set_answer.add(numbers[i]+numbers[j])
    return sorted(set_answer)