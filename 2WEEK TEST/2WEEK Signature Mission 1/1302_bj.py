word = {}
N = int(input())

for _ in range(N):
    name = input()

    if name in word:
        word[name] += 1
    else:
        word[name] = 1

book= dict(sorted(word.items()))
max = max(word, key=word.get)
print(max)
