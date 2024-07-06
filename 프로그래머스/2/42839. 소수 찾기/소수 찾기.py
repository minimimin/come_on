answer = 0
def findSosu(num):
    global answer
    for i in range(1, num):
        if i != 1 and num % i == 0:
            return 0
    if num>1:
        answer +=1
    return 1

def solution(numbers):
    global answer
    n = len(numbers)
    visited=[0 for _ in range(n)]
    check = set()
    def sunyeol(result,n):
        temp2 = int(result)
        if temp2 != 0:
            if not temp2 in check:
                findSosu(temp2)
                check.add(temp2)
        for i in range(n):
            if visited[i] == 0:
                temp3 = ""
                temp3 += result
                temp3 += numbers[i]
                visited[i] =1
                sunyeol(temp3,n)
                visited[i] =0
        
        
    for i in range(n):
        temp =""
        temp += numbers[i]
        visited[i]=1
        sunyeol(temp,n)
        visited[i]=0

    return answer