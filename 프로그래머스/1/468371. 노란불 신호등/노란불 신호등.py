import math
from functools import reduce

def lcm(a,b):
    return a*b//math.gcd(a, b)

def solution(signals):

    # 신호등별 전체 시간 구하기
    sinho_time = [sum(i) for i in signals]
    
    # 최소공배수 구하기(이 시간 넘으면 걍 -1임)
    lcm_time = reduce(lcm, sinho_time)
        
    # 신호등별 노란색 식별
    all_sinho = [[0]*n for n in sinho_time]
    for sinho in range(len(signals)):
        temp_idx = 0
        for green in range(signals[sinho][0]):
            all_sinho[sinho][temp_idx] = 1
            temp_idx += 1
        for yellow in range(signals[sinho][1]):
            all_sinho[sinho][temp_idx] = 2
            temp_idx += 1
        for red in range(signals[sinho][2]):
            all_sinho[sinho][temp_idx] = 1
            temp_idx += 1

    # 돌아가면서 모두가 2면 그 때 now_time 반환!
    now_time = 0
    while now_time <= lcm_time:
        temp_cnt = 0
        for idx in range(len(signals)):
            if all_sinho[idx][now_time%(sinho_time[idx])] == 2:
                temp_cnt += 1
        if temp_cnt == len(signals):
            return now_time+1
        now_time += 1
    
    return -1