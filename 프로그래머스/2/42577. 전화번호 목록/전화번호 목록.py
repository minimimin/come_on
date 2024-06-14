def solution(phone_book):
# 문자열 특성 이용하기!!
    temp_book = sorted(phone_book)
    # 전체 전화번호 수
    length = len(phone_book)
    # 전부 확인해보기
    for i in range(length-1):
    # 기준이 되는 전화번호 총 글자 수
        i_len = len(temp_book[i])
        # 전부 뒤 전화번호부랑 접두사로 확인해보기
        if temp_book[i] in temp_book[i+1][:i_len]:
            return False
    else:
        return True