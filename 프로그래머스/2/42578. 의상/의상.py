from collections import defaultdict

def solution(clothes):
    # 의상 종류에 따른 의상 이름 리스트 딕셔너리
    dic_clothes = defaultdict(int)
    for name, category in clothes:
        dic_clothes[category] += 1

    # 종류별 전체 옷이 몇 벌씩 있는지
    # 경우의 수에 따라 (각 요소+1)한걸 전부 곱한 후 -1 해주면 됨
    answer = 1
    for count in dic_clothes.values():
        answer *= (count + 1)
    return (answer - 1)