from collections import deque

def solution(n):
    answer = deque()
    str_n = str(n)
    for st in range(len(str_n)-1, -1, -1):
        answer.append(int(str_n[st]))
    return list(answer)