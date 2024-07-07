# 주어진 숫자들로 조합만들고
# 소수가 몇 개인지 판별
from itertools import permutations
import math

def making_num(number):
    find_all_johap = set()
    for length in range(1, len(number)+1):
        num_johap = permutations(number, length)
        for maked_number in num_johap:
            find_all_johap.add(int("".join(maked_number)))
    return find_all_johap

def sosu(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    else:
        jegobgeun = int(math.sqrt(num)) + 1
        for i in range(2, jegobgeun):
            if num % i == 0:
                return False
        return True

def solution(numbers):
    answer = 0
    all_number = making_num(numbers)
    for num in all_number:
        if sosu(num):
            answer += 1
    return answer