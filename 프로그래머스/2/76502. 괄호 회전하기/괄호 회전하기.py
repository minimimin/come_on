from collections import deque

def rotation(paren):
        ps = deque([])
        open_p = {"(":")", "[":"]", "{":"}"}
        close_p = {")", "]", "}"}
        if paren[0] in close_p:
            return False
        for p in paren:
            if p in open_p:
                ps.append(p)
            elif p in close_p:
                if ps:
                    if open_p[ps.pop()] != p:
                        return False
                else:
                    return False
        if ps:
            return False
        else:
            return True

def solution(s):
    answer = 0
    rotation_cnt = len(s)
    stack = deque(s)
    while rotation_cnt > 0:
        stack.append(stack.popleft())
        if rotation(stack):
            answer += 1
        rotation_cnt -= 1
    return 0 if answer <= 0 else answer