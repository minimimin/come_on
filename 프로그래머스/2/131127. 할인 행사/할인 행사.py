def solution(want, number, discount):
    answer = 0
    wants = {}
    for i in range(len(want)):
        wants[want[i]] = number[i]
    for idx in range(len(discount)-9):
        temp_wants = wants.copy()
        for ten in range(10):
            if discount[idx+ten] in temp_wants.keys() and temp_wants[discount[idx+ten]] >= 1:
                temp_wants[discount[idx+ten]] -= 1
        else:
            if sum(temp_wants.values()) == 0:
                answer += 1
    return answer