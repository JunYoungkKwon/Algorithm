def solution(phone_book):
    numbers = set(phone_book)
    for number in phone_book:
        for i in range(1, len(number)):
            if number[:i] in numbers:
                return False
    return True
