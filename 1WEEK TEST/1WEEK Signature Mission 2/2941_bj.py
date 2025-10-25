from tabnanny import check

dic= ["c=", "c-", "dz=","d-", "lj", "nj", "s=", "z="]
word = input()
for i in dic:
    word = word.replace(i, "1")

print(len(word))