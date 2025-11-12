def solution(prices):
    answer = []
    for i in range(len(prices)):
        std = prices[i]
        cnt = 0
        for j in range(i+1,len(prices)):
            cnt += 1
            if std > prices[j]:
                answer.append(cnt)
                break
        else:
            answer.append(cnt)
    return answer