# def solution(citations):
#     citations.sort()  # 논문 인용 순으로 정렬
#     thesis_len = len(citations)  # 논문 list 길이
#     cnt_thesis = 0 # 과학자의 최대 H-index
    
#     while cnt_thesis < thesis_len:  # 최대 H-index가 논문 전체 길이보다는 작음
#         if cnt_thesis < citations[thesis_len-cnt_thesis-1]: # h편 이상이 되어야하니까 list의 h번째 값이 최대 H-index보다 커야한다
#             cnt_thesis += 1 # 그러면 다음 검토를 위해 +1
#         else: # h번째 값이 최대 H-index랑 같거나 작으면
#             return cnt_thesis # 지금까지가 h-index니까 바로 반환
        
#     return cnt_thesis # 전부 h번째 값이 최대 H-index보다 큰 경우
def solution(citations):
    # 논문 중 h번 이상 인용된 논문이 h편 이상일 경우 나머지 논문이
    max_citations = 0
    for thesis in range(len(citations)+1):
        how_many_citations = list(filter(lambda x : x >= thesis, citations))
        if thesis <= len(how_many_citations):
            max_citations = thesis
    return max_citations            