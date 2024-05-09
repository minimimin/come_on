def solution(operations):
    answer = [0, 0]
    temp_list = []
    while operations:
        temp = operations.pop(0)
        if temp[0] == "I":
            temp_list.append(int(temp[2:]))
            temp_list.sort()
        elif temp[0] == "D":
            if temp_list:
                if temp[2] == "1":
                    temp_list.pop(-1)
                else:
                    temp_list.pop(0)
    if temp_list:
        answer = [max(temp_list), min(temp_list)]
    return answer