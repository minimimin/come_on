
def solution(numbers):
    string_num = list(map(str, numbers))
    string_num.sort(key=lambda num : num*4, reverse = True)
    if string_num[0] == '0':
        return '0'
    return "".join(string_num)