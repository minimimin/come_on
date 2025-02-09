def make_time(time):
    return int(time[:2])*60 + int(time[3:])

def check_opening(pos, op_start, op_end):
    if pos >= op_start and pos <= op_end:
        return op_end
    else:
        return pos
    
def make_str(time):
    min_time = str(time//60)
    sec_time = str(time%60)
    if len(min_time) != 2:
        min_time = '0' + min_time
    if len(sec_time) != 2:
        sec_time = '0' + sec_time           
    return min_time + ':' + sec_time

def solution(video_len, pos, op_start, op_end, commands):
    # 동영상 길이, 현재 재생위치, 오프닝시작, 오프닝 끝, 사용자 입력
    # 사용자 입력 제외 모든 글자는 5자리(00:00 이런식)
    # ① 글자를 숫자로 만들어서 생각할 것
    # "prev" 10초 전 이동(현재 위치가 10초 미만인 경우 영상의 처음 위치로 이동), 
    # "next" 10초 후 이동(남은 시간이 10초 미만일 경우 영상의 마지막 위치로 이동), 
    # 오프닝 건너뛰기 가능 = 현재 재생 위치가 오프닝 구간(op_start ≤ 현재 재생 위치 ≤ op_end)인 경우 자동으로 오프닝이 끝나는 위치로 이동
    # ② 명령어들 돌면서 검토할 것
    pos = make_time(pos)
    video_len = make_time(video_len)
    op_start = make_time(op_start)
    op_end = make_time(op_end)
    pos = check_opening(pos, op_start, op_end)
    for command in commands:
        if command == 'prev':
            if pos < 10:
                pos = 0
            else:
                pos -= 10
        elif command == 'next':
            if pos + 10 > video_len:
                pos = video_len
            else:
                pos += 10
        pos = check_opening(pos, op_start, op_end)
    # 최종 위치 리턴
    return make_str(pos)