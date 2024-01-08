from collections import defaultdict

def solution(participant, completion):
    participant_dic = defaultdict(int)
    for i in participant:
        participant_dic[i] += 1
    for j in completion:
        participant_dic[j] -= 1
        if participant_dic[j] == 0:
            del(participant_dic[j])
    for answer in participant_dic:
        return answer