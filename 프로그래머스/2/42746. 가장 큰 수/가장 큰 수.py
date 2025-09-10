def solution(numbers):
    num_str = list(map(str, numbers))
    num_str.sort(reverse=True, key=lambda x : x*3)
    if num_str[0] == "0":
        return "0"
    else:
        return "".join(num_str)