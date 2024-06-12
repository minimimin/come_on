def solution(phone_book):
    # temp_books = phone_book
    # for num in phone_book:
    #     length = len(num)
    #     for check_num in temp_books:
    #         if num == check_num:
    #             continue
    #         elif check_num[:length] == num:
    #             return False
    # return True

# 와..충격적,,문자열이니까 근처에 있는 것들 중심으로 보면 되는거구나...!
    temp_book = sorted(phone_book)
    length = len(phone_book)
    for i in range(length):
        i_len = len(temp_book[i])
        if i == 0:
            if temp_book[0] in temp_book[1][:i_len]:
                return False
        elif i == (length-1):
            if temp_book[i] in temp_book[i-1][:i_len]:
                return False
        else:
            if temp_book[i] in temp_book[i-1][:i_len] or temp_book[i] in temp_book[i+1][:i_len]:
                return False
    else:
        return True