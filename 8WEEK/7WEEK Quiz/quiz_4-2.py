from collections import deque
import math
feed = [180, 5000, 10, 600]
b_time = feed[0]
b_money = feed[1]
b_min = feed[2]
b_min_money = feed[3]

info_car = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
in_car = deque()
out_car = []
dict_ = {}


def change_Time(time_):
    h = int(time_[0:2]) * 60
    m = time_[3:5]
    return int(h) + int(m)


for x in info_car:
    if 'IN' in x:
        in_car.append(x)
    else:
        out_car.append(x)
while in_car:
    # 들어온 차 정보
    in_info_car = in_car.popleft().split(' ')
    # 시간 변경 분으로
    in_info_car[0] = change_Time(in_info_car[0])
    # 나가는 차
    # 포함, IN 여부 판단
    if not out_car or in_info_car[1] not in out_car:
        value_ = change_Time('23:59') - in_info_car[0]
    for i in range(len(out_car)):
        # 나가는 차 번호 일치
        if in_info_car[1] in out_car[i]:
            out_info_car = out_car.pop(i).split(' ')
            # 나가는 차 시간 변경
            out_info_car[0] = change_Time(out_info_car[0])
            value_ = out_info_car[0] - in_info_car[0]
            break
            # 저장되어 있지 않으면 추가, 되어 있으면 꺼내서 +
    if in_info_car[1] not in dict_:
        dict_[in_info_car[1]] = value_
    else:
        dict_[in_info_car[1]] = dict_.get(in_info_car[1]) + value_
    # 정렬
dict_ = dict(sorted(dict_.items()))
result_ = []
# 계산
for key, val in dict_.items():
    if val <= b_time:
        result_.append(b_money)
    else:
        money_ = b_money + math.ceil((val - b_time) / b_min) * b_min_money
        result_.append(int(money_))
print(result_)

# def solution(fees, records):
#     answer = []
#     stk = []
#     #올림 해야 됨 공식 수정 ㄱ
#     fee = fees[1] + (time - fees[0]) // fees[2] * fees[3]
#     for record in records:
#         t, n, is_io = record.split()
#         if is_io == "IN":
#             stk.append((t, n))
#         else:
#
#     return answer
#
# print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
# #[14600, 34400, 5000]