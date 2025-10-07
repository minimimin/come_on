from itertools import product

def solution(numbers, target):
    count = 0
    for cal_list in product(['+','-'], repeat=len(numbers)):
        temp_sum = 0
        for i in range(len(numbers)):
            if cal_list[i] == '+':
                temp_sum += numbers[i]
            else:
                temp_sum -= numbers[i]
        if temp_sum == target:
            count += 1
    return count