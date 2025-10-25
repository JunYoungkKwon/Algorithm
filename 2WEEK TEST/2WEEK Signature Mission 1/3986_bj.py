nice_word = 0

for i in range(int(input())):
    stk = []
    word = input()
    for ch in word:
        if stk:
            if stk[-1] == ch:
                stk.pop()

            else:
                stk.append(ch)
        else:
            stk.append(ch)
    if not stk:
        nice_word += 1


print(nice_word)

