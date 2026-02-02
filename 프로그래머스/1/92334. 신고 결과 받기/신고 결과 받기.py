from collections import defaultdict

def solution(id_list, report, k):
    singo_set = defaultdict(set)
    singo_cnt = defaultdict(int)
    find_mail_id = {i:0 for i in id_list}
    answer = []
    for singo in set(report):
        pihae, gahae = singo.split()
        singo_set[pihae].add(gahae)
        singo_cnt[gahae] += 1
    for check in singo_cnt:
        if singo_cnt[check] >= k:
            for name in id_list:
                if check in singo_set[name]:
                    find_mail_id[name] += 1
    for find_id in find_mail_id:
        answer.append(find_mail_id[find_id])
    return answer