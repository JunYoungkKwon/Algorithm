str_ans = input()
str_len = len(str_ans)
part_str = set()

for i in range(str_len):
    for j in range(i, str_len):
        temp = str_ans[i : j+1]
        # print(temp)
        part_str.add(temp)


print(len(part_str))