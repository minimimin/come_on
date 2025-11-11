# from collections import deque

def solution(s):
    find_couple = []
    for num in range(len(s)):
        now_num = s[num]
        if find_couple and find_couple[-1] == s[num]:
            find_couple.pop()
        else:
            find_couple.append(s[num])
    return 1 if not find_couple else 0