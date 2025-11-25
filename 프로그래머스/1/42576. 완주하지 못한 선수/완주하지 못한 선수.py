from collections import Counter

def solution(participant, completion):
    participant = Counter(participant)
    for person in completion:
        participant[person] -= 1
    for person in participant:
        if participant[person]:
            return person