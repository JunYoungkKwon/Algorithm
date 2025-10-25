import sys
input = sys.stdin.readline

for i in range(int(input())):
    word = input().rstrip()
    left = []
    right = []
    for ch in word:
        if ch == '<':
            if left:
                right.append(left.pop())
        elif ch == '>':
            if right:
                left.append(right.pop())
        elif ch == '-':
            if left:
                left.pop()
        else:
            left.append(ch)

    print("".join(left + right[::-1]))
    # right = list(reversed(right))
    # print("".join(left + right))








