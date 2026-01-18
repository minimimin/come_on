# from collections import defaultdict
from collections import Counter

def solution(want, number, discount):
    answer = 0
    wants = {}
    for i in range(len(want)):
        wants[want[i]] = number[i]
    for idx in range(len(discount)-9):
        check = Counter(discount[idx:idx+10])
        # for cnt_idx in range(idx, idx+10):
        #     check[discount[cnt_idx]] += 1
        if wants == check:
            answer += 1
    return answer