import heapq

def solution(scoville, K):
    count = 0
    hot_food = len(scoville)
    heapq.heapify(scoville)
    while hot_food > 1:
        first = heapq.heappop(scoville)
        hot_food -= 1
        if first >= K:
            return count
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + second*2)
        count += 1
    return count if heapq.heappop(scoville) >= K else -1