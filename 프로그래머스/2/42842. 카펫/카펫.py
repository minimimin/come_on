# 중앙은 노란색, 테두리는 갈색
# 갈색 격자의 수, 노란색 격자의 수
# [가로, 세로] 길이를 return

# 노란색 약수 조합 함수 하나 필요(조건 : 가로 >= 세로) => 리스트 리턴하기
# 약수들 리스트에 담았을 때 ((가로+2)+세로)*2 한 게 브라운이랑 똑같으면 리턴, 아니면 다음걸로 해보기

def imset(yellow):
    measure = []
    big_measure = yellow
    while big_measure and big_measure >= (yellow // big_measure):
        if not (yellow % big_measure):
            measure.append((big_measure, yellow // big_measure))
        big_measure -= 1
    return measure

def solution(brown, yellow):
    preliminary_tuple = imset(yellow)
    for w, l in preliminary_tuple:
        if (w + l + 2) * 2 == brown:
            return [ w+2, l+2 ]