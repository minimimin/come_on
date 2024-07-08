# 갈색은 (가로 + 세로 - 2)*2
# 노란색은 (가로-2)*(세로-2)

def solution(brown, yellow):
    for i in range(brown//2-1, 0, -1):
        for j in range(brown//2-1, 0, -1):
            if (i + j - 2) * 2 == brown and (i-2)*(j-2) == yellow:
                return [i, j] if i >= j else [j, i]