phone_book = ["119", "97674223", "1195524421"]
def solution(phone_book):
    phone_book.sort()
    answer = True
    for k in range(len(phone_book)-1):
        a = phone_book[k]
        b = phone_book[k+1]
        print(b[:len(b)])
        if a == b[0:len(b)]:
            print(b[:len(b)])
            answer = False
            print(answer)
            return False
    print(answer)
    return answer

solution(phone_book)
# phone_book = "1195524421"
# print(phone_book[:])
