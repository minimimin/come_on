# def solution(participant, completion):
#     participant.sort()
#     completion.sort()
#     for i in range(len(completion)):
#         if participant[i] != completion[i]:
#             return participant[i]
#     return participant[-1]

# def solution(participant, completion):
#     for i in participant:
#         if i not in completion:
#             return i
        
def solution(participant, completion):
    dict_part = {}
    for finisher in completion:
        if finisher in dict_part:
            dict_part[finisher] += 1
        else:
            dict_part[finisher] = 1
    for name in participant:
        if name in dict_part and dict_part[name]:
            dict_part[name] -= 1
        else:
            return name
    