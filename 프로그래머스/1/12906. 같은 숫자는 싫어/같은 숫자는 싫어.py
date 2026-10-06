def solution(arr):
    answer = []
    now_num = -1
    for i in arr:
        if now_num == i:
            continue
        else:
            now_num = i
            answer.append(i)
    return answer