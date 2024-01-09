from collections import deque
def solution(arr):
    answer = deque()
    for i in arr:
        if not answer or i != answer[-1]:
            answer.append(i)
    return list(answer)