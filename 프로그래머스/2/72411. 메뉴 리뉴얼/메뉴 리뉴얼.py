from collections import Counter
# from collections import defaultdict
from itertools import combinations

def solution(orders, course):
    answer = []
    for course_len in course:
        menu = []
        for order in orders:
            menu += combinations(sorted(order), course_len)
        count_johap = Counter(menu)
        if count_johap and max(count_johap.values()) > 1:
            max_johap = max(count_johap.values())
            for find in count_johap:
                if count_johap[find] == max_johap:
                    answer.append(''.join(find)) 
    return sorted(answer)