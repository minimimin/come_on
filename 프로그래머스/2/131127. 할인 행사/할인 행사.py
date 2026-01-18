# from collections import defaultdict
from collections import Counter

def solution(want, number, discount):
    answer = 0
    wants = {}
    for i in range(len(want)):
        wants[want[i]] = number[i]
    for idx in range(len(discount)-9):
        if wants == Counter(discount[idx:idx+10]):
            answer += 1
    return answer