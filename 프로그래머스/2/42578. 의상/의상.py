from collections import defaultdict

def solution(clothes):
    # 각 행은 [이름, 종류]로 구성
    # 종류별로 몇 개 있는지 카운트
    # 종류별로 (1(안입기)+개수)만큼의 선택지 있음 => 각 선택지마다 곱하기
    # 전부 다 안입을 수는 없음 = 1 빼기
    count_clothes = defaultdict(int)
    for _, t in clothes:
        count_clothes[t] += 1
    answer = 1
    for ty in count_clothes:
        answer *= (count_clothes[ty]+1)
    return answer - 1