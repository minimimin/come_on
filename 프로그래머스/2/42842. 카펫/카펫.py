# 갈색은 (가로 + 세로-2)*2
# 노란색은 (가로-2)*(세로-2) = 약수조합으로 구해도 된다

def solution(brown, yellow):
    for i in range(3, brown//2+1):
        if yellow % (i-2) == 0:
            j = (yellow // (i-2)) + 2
            if (i+j-2)*2 == brown:
                return [i, j] if i >= j else [j, i]