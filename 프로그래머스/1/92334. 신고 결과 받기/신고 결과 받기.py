from collections import defaultdict

def solution(id_list, report, k):
    # 한 번에 한 유저 신고, 동일한 유저 신고 횟수는 1회
    # k번 이상 신고되면 이용 정지 => 신고한 모든 유저는 메일로 안내
    # 각 유저별로 메일 받은 횟수 return
    # 1) defaultdict으로 list형(각 유저별 신고한 명단), int형(신고 당한 횟수)
    # 2) 0번째 append 1번째, 1번쨰 += 1 전체 다 넣고 int dict에서 k 이상인 명단 추출(list화 or set에 넣어도 됨)
    # 3) id 순서대로 in 확인 후 cnt 넣기
    singo = defaultdict(set)
    report_cnt = defaultdict(set)
    singo_list = []
    answer = []
    for report_con in report:
        singo[report_con.split()[0]].add(report_con.split()[1])
        report_cnt[report_con.split()[1]].add(report_con.split()[0])
    for man in report_cnt:
        if len(report_cnt[man]) >= k:
            singo_list.append(man)
    for id_singo in id_list:
        cnt = 0
        for find_singo in singo[id_singo]:
            if find_singo in singo_list:
                cnt += 1
        answer.append(cnt)
    return answer