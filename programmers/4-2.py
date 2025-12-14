def solution(numbers):
    nums = list(map(str, numbers))

    # 문자열 비교 기준 정렬
    nums.sort(key=lambda x: x * 3, reverse=True)

    # 0만 있는 경우 처리
    answer = ''.join(nums)
    return '0' if answer[0] == '0' else answer
