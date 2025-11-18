def solution(s):
    memo = []
    answer = 0
    comm = s.split()
    for num in comm:
        if num == 'Z':
            answer -= memo.pop()
        else:
            answer += int(num)
            memo.append(int(num))
    return answer