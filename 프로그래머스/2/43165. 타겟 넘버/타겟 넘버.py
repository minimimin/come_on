def solution(numbers, target):

    def dfs(now_idx, now_num):
        if now_idx == len(numbers):
            if now_num == target:
                return True
            return False
        
        return dfs(now_idx+1, now_num-numbers[now_idx]) + dfs(now_idx+1, now_num+numbers[now_idx])

    return dfs(0, 0)