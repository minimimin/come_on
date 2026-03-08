from itertools import combinations
from collections import Counter

def solution(friends, gifts):
    gift_jisu = {friend:0 for friend in friends}
    # 각 사람별 선물지수 count하기
    
    relation = set(johap for johap in combinations(friends, 2))
    # 나올 수 있는 관계 조합에서 선물 받을 사람 구하기
    
    gift_switch = Counter(gifts)
    # 주고받은 횟수 count하기
    
    next_gift = {friend:0 for friend in friends}
    # 각 사람별 다음달 받을 선물 count하기
    
    # 선물지수 구하기
    for man in gifts:
        check = man.split(" ")
        gift_jisu[check[0]] += 1
        gift_jisu[check[1]] -= 1

    # 관계별 더 많이 받을 사람 구하기
    for fri_jo in relation:
        give = fri_jo[0] + " " + fri_jo[1]
        rec = fri_jo[1] + " " + fri_jo[0]
        if gift_switch[give] or gift_switch[rec]:
            if gift_switch[give] > gift_switch[rec]:
                next_gift[fri_jo[0]] += 1
            elif gift_switch[give] < gift_switch[rec]:
                next_gift[fri_jo[1]] += 1
            else:
                if gift_jisu[fri_jo[0]] > gift_jisu[fri_jo[1]]:
                    next_gift[fri_jo[0]] += 1
                elif gift_jisu[fri_jo[0]] < gift_jisu[fri_jo[1]]:
                    next_gift[fri_jo[1]] += 1       

        else:
            if gift_jisu[fri_jo[0]] > gift_jisu[fri_jo[1]]:
                next_gift[fri_jo[0]] += 1
            elif gift_jisu[fri_jo[0]] < gift_jisu[fri_jo[1]]:
                next_gift[fri_jo[1]] += 1
        
    # 제일 많이 받을 사람의 최대값 찾기
    return max(next_gift.values())