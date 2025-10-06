def solution(number, k):
    answer = []
    len_num = len(number)

    for num in number:
        while k and answer:
            last_num = answer.pop()
            if last_num < num:
                k -= 1
            else:
                answer.append(last_num)
                break
        answer.append(num)
        
    return "".join(answer) if len(answer) == len_num-k else "".join(answer[:len_num-k])