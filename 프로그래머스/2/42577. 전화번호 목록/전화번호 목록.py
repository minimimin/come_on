# def solution(phone_book):
#     sorted_phone_book = sorted(phone_book)
#     for i in range(len(phone_book)-1):
#         len_num = len(sorted_phone_book[i])
#         if sorted_phone_book[i] == sorted_phone_book[i+1][:len_num]:
#                 return False
#     return True

def solution(phone_book):
    s = set(phone_book)  # 모든 번호를 해시셋에 저장
    for num in phone_book:
        # num의 모든 "진접두어"가 s에 있는지 확인
        for i in range(1, len(num)):
            if num[:i] in s:
                return False
    return True
