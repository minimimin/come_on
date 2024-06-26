# 뒤에 나보다 작은 것들이 있는지 찾기
# 있으면 그 전까지 count(해당index - 현재index)
# 없으면 남은 요소 전부 count(전체 길이 - (현재index+1))
# 뒤에 나보다 작은 애들 있는지 찾는게 일인 거 같다..!
# from collections import deque

def solution(prices):
    answer = []
    stock_length = len(prices)
    for now_idx in range(stock_length):
        if now_idx == stock_length-1:
            answer.append(0)
        else:
            count = 0
            for next_idx in range(now_idx + 1, stock_length):
                count += 1
                if prices[now_idx] > prices[next_idx]:
                    break
            answer.append(count)
    return answer