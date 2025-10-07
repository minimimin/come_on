def solution(numbers, target):
    def dfs(now_idx, now_sum):
        if now_idx == len(numbers) and now_sum == target:
            return 1
        elif now_idx >= len(numbers):
            return 0
            
        return dfs(now_idx+1, now_sum + numbers[now_idx]) + dfs(now_idx+1, now_sum - numbers[now_idx])
        
    return dfs(1, 0 + numbers[0]) + dfs(1, 0 - numbers[0])