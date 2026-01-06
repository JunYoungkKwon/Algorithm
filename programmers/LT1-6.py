from itertools import permutations
import re


def solution(expression):
    # 1. 숫자와 연산자 분리
    nums = list(map(int, re.findall(r'\d+', expression)))
    ops = re.findall(r'[\+\-\*]', expression)

    # 2. 가능한 연산자 우선순위 조합
    op_set = set(ops)
    op_perms = permutations(op_set)

    max_value = 0

    for perm in op_perms:
        tmp_nums = nums[:]
        tmp_ops = ops[:]

        for op in perm:
            i = 0
            while i < len(tmp_ops):
                if tmp_ops[i] == op:
                    # 연산
                    if op == '+':
                        res = tmp_nums[i] + tmp_nums[i + 1]
                    elif op == '-':
                        res = tmp_nums[i] - tmp_nums[i + 1]
                    else:  # '*'
                        res = tmp_nums[i] * tmp_nums[i + 1]

                    # 숫자와 연산자 리스트 업데이트
                    tmp_nums[i] = res
                    del tmp_nums[i + 1]
                    del tmp_ops[i]
                else:
                    i += 1

        max_value = max(max_value, abs(tmp_nums[0]))

    return max_value


# 테스트
expression = "100-200*300-500+20"
print(solution(expression))  # 결과: 60420
