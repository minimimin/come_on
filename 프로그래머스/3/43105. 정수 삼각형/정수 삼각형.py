def solution(triangle):
    answer = 0
    len_triangle = len(triangle)
    twin_triangle = [[0]*(i+1) for i in range(len_triangle-1)]
    twin_triangle.append(triangle[len_triangle-1])
    for floor in range(len_triangle-2,0,-1):
        len_floor = len(twin_triangle[floor])
        for i in range(len_floor):
            twin_triangle[floor][i] = triangle[floor][i] + max(twin_triangle[floor+1][i], twin_triangle[floor+1][i+1])
    return triangle[0][0] + max(twin_triangle[1][0], twin_triangle[1][1])