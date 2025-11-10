def solution(dirs):
    direction = {"U":(-1,0), "D":(1,0), "R":(0,1), "L":(0,-1)}
    now_x, now_y = 0, 0
    count_road = set()
    for command in dirs:
        plus_x, plus_y = direction[command]
        if now_x + plus_x >= -5 and now_x + plus_x  <= 5 and now_y + plus_y >= -5 and now_y + plus_y <= 5:
            count_road.add((now_x, now_y, now_x + plus_x, now_y + plus_y))
            count_road.add((now_x + plus_x, now_y + plus_y, now_x, now_y))
            now_x += plus_x
            now_y += plus_y
    return len(count_road)//2