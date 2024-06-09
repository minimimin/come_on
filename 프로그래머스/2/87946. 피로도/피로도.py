# dungeons 길이로 순열 구해서 다 해보기!
# 최소 필요 피로도가 더 크면 리턴하기
# 카운트 해놓은 거 담을 리스트도 필요하다
# 
from itertools import permutations

# def check_all(index_list):
#     global k, dungeons
#     now_k = k
#     dungeon_count = 0
#     for index in index_list:
#         if now_k < dungeons[index][0]:
#             return dungeon_count
#         else:
#             now_k -= dungeons[index][1]
#             dungeon_count += 1
#     return dungeon_count

def solution(k, dungeons):
    permu = permutations([_ for _ in range(len(dungeons))], len(dungeons))
    # answer = list(map(check_all, permu))
    answer = []
    for index_list in permu:
        now_k = k
        dungeon_count = 0
        for index in index_list:
            if now_k < dungeons[index][0]:
                answer.append(dungeon_count)
                break
            else:
                now_k -= dungeons[index][1]
                dungeon_count += 1
        answer.append(dungeon_count)
    return max(answer)