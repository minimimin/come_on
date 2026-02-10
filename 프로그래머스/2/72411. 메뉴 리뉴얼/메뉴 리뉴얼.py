from collections import defaultdict
from itertools import combinations

def solution(orders, course):
    answer = []
    check = {}
    for num in course:
        check[num] = defaultdict(int)
        
    for idx in range(len(orders)-1):
        std_set = set(orders[idx])
        for next_i in range(idx+1,len(orders)):
            exp_set = set(orders[next_i])
            temp_course = []
            for alp in exp_set:
                if alp in std_set:
                    temp_course.append(alp)
            # 현재 상태에서 나온걸로 길이별 조합을 만들어야하는데,,
            for lens in course:
                johap = combinations(temp_course, lens)
                for alp_jo in johap:
                    sor_alp_jo = sorted(alp_jo)
                    check[lens]["".join(sor_alp_jo)] += 1
            
    for num_cou in check:
        if not check[num_cou]:
            continue
        max_cou = max(check[num_cou].values())
        for dish in check[num_cou]:
            if check[num_cou][dish] == max_cou:
                answer.append(dish)
    return sorted(answer)