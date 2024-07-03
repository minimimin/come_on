def solution(numbers):
    num_str = [str(num) for num in numbers]
    num_str.sort(reverse=True, key=lambda x : x*4)
    answer = "".join(num_str)
    return answer if answer[0] != "0" else "0"