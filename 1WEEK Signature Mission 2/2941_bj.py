str = input()
check = ["c=","c-","dz=","d-","lj","nj","s=","z="]
for i in check:
    str = str.replace(i, "1")

print(len(str))
