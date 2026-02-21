from collections import Counter
    
def solution(participant, completion):
    com_dict = Counter(completion)
    part_dict = Counter(participant)
    for answer in (part_dict - com_dict):
        return answer