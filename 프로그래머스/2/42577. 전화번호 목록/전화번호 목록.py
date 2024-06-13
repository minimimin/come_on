def solution(phone_book):
    temp_books = set(phone_book)
    for num in phone_book:
        length = len(num)
        for index in range(length):
            if num[0:index] in temp_books:
                return False
    return True