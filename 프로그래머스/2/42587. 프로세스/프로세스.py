def solution(priorities, location):
    answer = 0
    find_num = (priorities[location], location)
    im_que = []
    im_max_list = sorted(priorities)
    im_max_list.reverse()
    for i in range(len(priorities)):
        im_que.append((priorities[i], i))
    while im_que:
        if im_que[0][0] == im_max_list[0]:
            answer += 1
            if im_que[0] == find_num:
                return answer
            im_max_list.pop(0)
            im_que.pop(0)
        else:
            a = im_que.pop(0)
            im_que.append(a)
    return answer