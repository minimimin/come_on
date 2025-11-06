def solution(arr1, arr2):
    # 행렬의 곱셈은 가로*세로 합
    # [0][0] = [0][0]*[0][0] + [0][1]*[1][0]
    # [0][1] = [0][0]*[1][0] + [0][1]*[1][1]
    # [1][0] = [1][0]*[0][0] + [1][1]*[1][0]
    # 행렬가로세로길이
    arr_row = len(arr1)
    arr_col = len(arr2[0])
    arr_common = len(arr1[0])
    # arr1의 행(len(arr1[0])), arr2의 열(len(arr2))은 길이가 동일하다
    answer = [[0]*arr_col for _ in range(arr_row)]
    for r in range(arr_row):
        for c in range(arr_col):
            for k in range(arr_common):
                answer[r][c] += arr1[r][k]*arr2[k][c]
    return answer