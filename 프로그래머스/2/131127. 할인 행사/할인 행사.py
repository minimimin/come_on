from collections import defaultdict

def solution(want, number, discount):
    wants = defaultdict(int)
    answer = 0
    for prod_idx in range(len(want)):
        wants[want[prod_idx]] = number[prod_idx]
    for idx in range(len(discount)-9):
        check = defaultdict(int)
        for cnt_idx in range(idx, idx+10):
            check[discount[cnt_idx]] += 1
        if wants == check:
            answer += 1
    return answer