def solution(phone_book):
    temp_book = sorted(phone_book)
    length = len(phone_book)
    for i in range(length-1):
        i_len = len(temp_book[i])
        if temp_book[i] in temp_book[i+1][:i_len]:
                return False
    else:
        return True