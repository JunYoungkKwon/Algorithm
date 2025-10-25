
word = input().strip()

for i in range (len(word)):
    if i == 0:
        print(word[0], end="")
    else:
        if word[i] == '-':
            print(word[i+1], end="")


