from collections import defaultdict
t_dict = defaultdict(int)














































def cal_date(p_date, period):
    p_date = p_date.replace(".", " ")
    year, mon, day = p_date.split()
    # print(f"{year} {mon} {day} {period}")
    year_plus = (int(mon) + int(period)) // 12
    year = int(year) + year_plus
    mon = (int(mon) + int(period)) % 12
    day = int(day) - 1
    # print(f" {int(mon)} {int(period)}")
    if day == 0:
        day = 28
        mon = mon -1
        if mon < 1:
            mon = 12+ mon
            year = year -1


    # print(f"{year} {mon} {day}")
    return year, mon, day

def solution(today, terms, privacies):
    answer = []
    today = today.replace(".", " ")
    year, mon, day = today.split()
    # print(f"{year} {int(mon)} {day}")

    for i in range(len(terms)):
       t, period = terms[i].split()
       t_dict[t] = period
    # print(t_dict)
    for i in range(len(privacies)):
        p_date, t = privacies[i].split()
        for key, value in t_dict.items():
            if key == t:
                y, m, d = cal_date(p_date, value)
                # print(f"{p_date} {value}")
                if int(year) > y:
                    answer.append(i+1)
                else:
                    if int(mon) > m:
                        answer.append(i + 1)
                    else:
                        if int(day) > d:
                            answer.append(i + 1)




    return answer

print(solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))
