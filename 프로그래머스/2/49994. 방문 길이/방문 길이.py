# 처음 걸어본 길 길이 구하기 visited에 0인 것만 cnt
# 경계를 넘어가는 명령어 무시(상하좌우 5)
# 명령은 UDRL만 존재
def solution(dirs):
    answer = 0
    max_size = 5
    min_size = -5
    visited = set()
    move = {'U' : (-1,0), 'D' : (1,0), 'R' : (0,1), 'L' : (0,-1)}
    now_me = (0,0)

    for move_dir in dirs:
        check_r = now_me[0]+move[move_dir][0]
        check_l = now_me[1]+move[move_dir][1]
        next_me = (check_r, check_l)
        if (min_size <= check_r <= max_size) and (min_size <= check_l <= max_size):
            if (now_me, next_me) not in visited:
                visited.add((now_me, next_me))
                visited.add((next_me, now_me))
                answer += 1
            now_me = next_me
    return answer