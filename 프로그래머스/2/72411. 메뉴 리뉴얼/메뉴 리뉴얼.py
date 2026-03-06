from collections import defaultdict
from itertools import combinations

def solution(orders, course):
    answer = []
    com_course = {x:defaultdict(int) for x in course}
    for order in orders:
        for num in course:
            if len(order) >= num:
                for johap in combinations(sorted(order), num):
                    com_course[num][johap] += 1
            else:
                break
    for num_course in com_course:
        if com_course[num_course]:
            choose_course = max(com_course[num_course].values())
            if choose_course > 1:
                for menu_johap in com_course[num_course]:
                    if com_course[num_course][menu_johap] == choose_course:
                        answer.append(''.join(menu_johap))
    answer.sort()
    return answer