def solution(board, moves):
    boom_cnt = 0
    basket = []
    n = len(board)
    for col in moves:
        for line in range(n):
            if board[line][col-1]:
                if basket and basket[-1] == board[line][col-1]:
                    boom_cnt += 2
                    basket.pop()
                else:
                    basket.append(board[line][col-1])
                board[line][col-1] = 0
                break
    return boom_cnt