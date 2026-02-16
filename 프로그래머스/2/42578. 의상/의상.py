from collections import defaultdict

def solution(clothes):
    closet = defaultdict(int)
    answer = 1
    for name, types in clothes:
        closet[types] += 1
    for clo_type in closet:
        answer *= (closet[clo_type]+1)
    return answer-1