from itertools import permutations
from functools import partial

def check_all(index_list, k, dungeons):
    now_k = k
    dungeon_count = 0
    for index in index_list:
        if now_k < dungeons[index][0]:
            return dungeon_count
        else:
            now_k -= dungeons[index][1]
            dungeon_count += 1
    return dungeon_count

def solution(k, dungeons):
    permu = permutations([_ for _ in range(len(dungeons))], len(dungeons))
    check_all_partial = partial(check_all, k=k, dungeons=dungeons)
    answer = list(map(check_all_partial, permu))
    return max(answer)