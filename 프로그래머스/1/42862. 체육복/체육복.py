from copy import deepcopy

def solution(n, lost, reserve):
    count = n # 몇 명이 체육복 입는지 체크
    lost.sort()
    check = deepcopy(lost)
    for i in lost:
        for k in [0, -1, 1]:
            if (i+k) in reserve:
                if (i+k) in lost and k!= 0:
                    continue
                reserve.remove(i+k)
                check.remove(i)
                break
    return count - len(check)
            
    # n : 전체 학생 수
    # lost : 체육복 잃어버린 학생 수(앞뒤 번호만 빌릴 수 있음)
    # reserve : 여분의 체육복이 있는 학생 수
    # 전체 몇 명이 체육복 입을 수 있는지 고르기    