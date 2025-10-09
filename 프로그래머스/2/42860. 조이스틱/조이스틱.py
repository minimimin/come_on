def solution(name):
    answer = 0
    # 상하 => min((ord(문자)-ord('A')), (91-ord(문자)))
    # 조이스틱 상하는 알파벳 26자(N:13이 최대, 나머지는 반갈라서 생각, A : 65, N:78, Z:90)
    for string in name:
        answer += min((ord(string)-ord('A')), (1+ord('Z')-ord(string)))
    print(answer)
    # 좌우 : 연속된 A 건너뛰고 생각해보기(최초 시작값, 종료값 사이 간격 생각하기) 
    # => min(len(name)-1, 2*x+(len(name)-y), x+2*(len(name)-y)
    l = len(name)
    temp_rl = [l-1]
    for idx in range(0,l-1):
        if name[idx+1] == 'A':
            x = idx
            for y in range(x+1, l):
                if name[y-1] == 'A' and name[y] != 'A':
                    temp_rl.append(min(2*x+l-y, x+2*(l-y)))
                    break
            else:
                temp_rl.append(x)
    return min(temp_rl)+answer