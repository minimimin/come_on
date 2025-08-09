# 전체 나와있는 것들 중에서 반만큼만 가져갈 수 있다. (len(num)//2 만큼만! => 어차피 짝수로 주어진다고 함)

# def solution(nums):
#     temp_dic = {}
#     length = len(nums)
#     for i in nums:
#         if i in temp_dic:
#         # if temp_dic[i]:
#             temp_dic[i] += 1
#         else:
#             temp_dic[i] = 1
#     if len(temp_dic) > (length//2):
#         return length//2
#     else:
#         return len(temp_dic)

from collections import defaultdict

def solution(nums):
    catch_num = len(nums)//2
    default_dict = defaultdict(int)
    for phonecket in nums:
        default_dict[phonecket] += 1
    return min(len(default_dict), catch_num)
    