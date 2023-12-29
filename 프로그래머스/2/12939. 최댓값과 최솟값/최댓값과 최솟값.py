def solution(s):
    s = s.split()
    num_list = [int(i) for i in s]
    return  str(min(num_list)) + ' ' + str(max(num_list))