def solution(citations):
    answer = 0
    citations.sort()
    thesis_len = len(citations)
    cnt_thesis = 0
    while cnt_thesis < thesis_len:
        if cnt_thesis < citations[thesis_len-cnt_thesis-1]:
            cnt_thesis += 1
            answer = cnt_thesis
        else:
            break
            # if answer >= cnt_thesis:
            #     return answer
            # else:
            #     cnt_thesis -= 1
        
    return answer