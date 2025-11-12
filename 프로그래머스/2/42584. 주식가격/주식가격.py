def solution(prices):
    sec = len(prices)
    answer = [0]*sec
    stack = [0]
    for i in range(1, sec):
        while stack and prices[stack[-1]] > prices[i]:
            down = stack.pop()
            answer[down] = i-down
        stack.append(i)
    if stack:
        for idx in stack:
            answer[idx] = (sec-1)-idx
    return answer