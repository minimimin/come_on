def solution(numbers, target):
    def dfs(now_idx, now_sum):
        if now_idx == len(numbers)-1 and now_sum == target:
            return 1
        elif now_idx >= len(numbers)-1:
            return 0
        return dfs(now_idx+1, now_sum + numbers[now_idx+1]) + dfs(now_idx+1, now_sum - numbers[now_idx+1])
    return dfs(0, numbers[0]) + dfs(0, -numbers[0])