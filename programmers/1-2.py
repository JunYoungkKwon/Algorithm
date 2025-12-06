nums = [3,1,2,3]
def solution(nums):
    max_num = len(nums) // 2
    dic = {}
    for k in nums:
        dic[k] = dic.get(k, 0) + 1
    if max_num <= len(dic):
        return max_num
    else:
        return len(dic)

solution(nums)