from heapq import heapify, heappush, heappop

def solution(scoville, K):
    heapify(scoville)
    count = 0
    while scoville:
        not_spicy_fir = heappop(scoville)
        if not_spicy_fir >= K:
            return count
        if not scoville:
            return -1
        not_spicy_sec = heappop(scoville)
        heappush(scoville, not_spicy_fir+not_spicy_sec*2)
        count += 1

    if not scoville:
        return -1