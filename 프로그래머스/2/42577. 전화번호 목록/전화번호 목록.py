# def solution(phone_book):
# # 문자열 특성 이용하기!!
#     temp_book = sorted(phone_book)
#     # 전체 전화번호 수
#     length = len(phone_book)
#     # 전부 확인해보기
#     for i in range(length-1):
#     # 기준이 되는 전화번호 총 글자 수
#         i_len = len(temp_book[i])
#         # 전부 뒤 전화번호부랑 접두사로 확인해보기
#         if temp_book[i+1].startswith(temp_book[i]):
#             return False
#     else:
#         return True
    
# def solution(phone_book):
#     # 접두어면 false, 아니면 true
#     all_phone_number = len(phone_book)
#     for std_idx in range(all_phone_number):
#         for com_idx in range(all_phone_number):
#             if std_idx != com_idx and phone_book[std_idx] in phone_book[com_idx]:
#                 return False
#     return True
                
# 일단 짧은 순으로 다 꺼내서 확인해보나..?
# 처음 것 꺼내서 그것만큼 돌려보나..?
def solution(phone_book):
    sorted_phone_book = sorted(phone_book)
    for i in range(len(phone_book)-1):
        len_num = len(sorted_phone_book[i])
        if sorted_phone_book[i] == sorted_phone_book[i+1][:len_num]:
                return False
    return True