def solution(n):
    num = 0
    for i in range(1, n+1):
        if not (n % i):
            num += i
    return num