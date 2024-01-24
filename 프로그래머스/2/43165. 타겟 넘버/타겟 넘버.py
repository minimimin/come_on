count = 0

def DFS(calcul, point, numbers, target):
    global count
    if point == len(numbers):
        if target == calcul:
            count += 1
        return
    DFS(calcul + numbers[point], point+1, numbers, target)
    DFS(calcul - numbers[point], point+1, numbers, target)

def solution(numbers, target):
    global count
    DFS(0, 0, numbers, target)
    return count