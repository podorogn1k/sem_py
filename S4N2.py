f = open("numbers.txt")
num = []
flag = True
fl = 1
for line in f:
    if (line[0] == "-"):
        line = line.replace("-", "", 1)
        fl = -1
    if (line.strip().isdigit()):
        num.append(fl * int(line))
        fl = 1
    else:
        flag = False
        break
ans = open("result.txt", "w")
if (flag):
    ans.write(str(min(num)) + "\n")
    ans.write(str(max(num)) + "\n")
    ans.write(str(sum(num)/len(num)) + "\n")
else:
    ans.write("error: not all string objects are numbers")