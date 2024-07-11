def solution(numbers):
    num_str = list(map(str, numbers))
    num_str.sort(reverse=True, key=lambda x : x*3)
    answer = "".join(num_str)
    return answer if answer[0] != "0" else "0"