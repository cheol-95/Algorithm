def solution(phone_book):
    length = list(map(len, phone_book))
    for i,v in enumerate(phone_book):
        for j in phone_book:
            if v == j:
                continue
            if v == j[:length[i]]:
                return False
    return True


# phone_book = ["12", "123", "1235", "567", "88"]
phone_book = ["123", "456", "789"]
print(solution(phone_book))