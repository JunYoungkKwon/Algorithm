def solution(new_id):
    answer = ''
    del_idx = []
    com_cnt = 0
    # 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
    new_id = new_id.lower()
    print(new_id)
    # 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
    for char in new_id:
        if char not in "1234567890abcdefghijklmnopqrstuvwxyz.-_":
            new_id = new_id.replace(char, '')
    print(new_id)
    # 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
    for i in range(len(new_id)):
        if new_id[i] == ".":
            com_cnt += 1
        else:
            com_cnt = 0

        if com_cnt >= 2:
            com_cnt -= 1
            del_idx.append(i)
    new_id = list(new_id)
    first = 0
    for idx in del_idx:
        if first == 0:
            del (new_id[idx])
            first += 1
        else:
            del (new_id[idx-first])
            first += 1
    new_id = "".join(new_id)
    new_id = list(new_id)
    print(new_id)
    # 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    if new_id[0] == ".":
        new_id[0] = ""
    if new_id[-1] == ".":
        new_id[-1] = ""
    new_id = "".join(new_id)
    new_id = list(new_id)
    print(new_id)
    # 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
    if len(new_id) == 0:
        new_id.append("a")
    print(new_id)
    # 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    #      만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
    if len(new_id) > 15:
        new_id = new_id[:15]
        if new_id[-1] == ".":
            del new_id[-1]
    print(new_id)
    # 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    if len(new_id) <= 2:
        new_id.append(new_id[-1])
        if len(new_id) != 3:
            new_id.append(new_id[-1])

    new_id = "".join(new_id)
    answer = new_id
    print(new_id)

    return answer

print(solution("123_.def"))