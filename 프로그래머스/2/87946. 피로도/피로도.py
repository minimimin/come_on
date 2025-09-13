from itertools import permutations

def solution(k, dungeons):
    max_count = 0
    all_dungeons = len(dungeons)
    soonyeol = list(permutations([i for i in range(all_dungeons)], all_dungeons))
    for path in soonyeol:
        if max_count >= all_dungeons:
            return max_count
        count_dungeons = 0
        now_k = k
        for dungeon in path:
            if dungeons[dungeon][0] <= now_k:
                now_k -= dungeons[dungeon][1]
                count_dungeons += 1
            else:
                if count_dungeons > max_count:
                    max_count = count_dungeons
                break
        if count_dungeons > max_count:
            max_count = count_dungeons 
    return max_count